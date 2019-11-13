# coding=utf-8
import json
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.http import HttpResponseForbidden, HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.urls import reverse
from .models import Category, Section, Thread, Post
from .forms import PostForm, ThreadPageForm, ThreadForm


class CategoriesListView(ListView):  # used
    """Отображает список категорий."""
    queryset = Category.objects.filter(is_hidden=False).order_by('sort_key')
    context_object_name = 'categories'
    template_name = 'forum/categories.html'
    paginate_by = 20


def thread(request, category_id, section_id, pk):  # used
    """Показать тред на форуме."""
    thread = get_object_or_404(Thread.objects.select_related('section', 'section__category'), id=pk)
    posts = Post.objects.filter(thread=thread)

    # form_class = PostForm if request.user.is_authenticated() else PostCaptchaForm
    # form_class = PostForm
    # if request.POST or request.FILES:
    #     form = form_class(request.POST, request.FILES)
    # else:
    #     form = form_class()
    # user = request.user if request.user.is_authenticated() else None
    # anchor = ''
    #
    # if request.POST and thread.comments_allowed:
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.thread_id = pk
    #         post.user = user
    #         post.user_ip = (request.META.get('HTTP_X_FORWARDED_FOR', '') or
    #                         request.META.get('REMOTE_ADDR'))
    #         if ',' in post.user_ip:
    #             post.user_ip = post.user_ip.split(',')[0]
    #         username = request.user.username if user is not None else None
    #         if not is_banned(post.user_ip, username, post.text):
    #             post.save()
    #
    #             return redirect(post)
    #         else:
    #             error_text = (
    #                 'Ваш комментарий не может быть добавлен, '
    #                 'так как не удовлетворяет условиям модерации. '
    #                 '<a target="_blank" href="https://gorodkirov.ru/info/rules/">Правила публикации</a>'
    #             )
    #             form_add_error(form, 'text', error_text)
    #             anchor = '#addcomment'
    #     else:
    #         anchor = '#addcomment'

    return render(request, 'forum/thread.html',  {
         'category_id': category_id,
         'section_id': section_id,
         'thread': thread,
         'posts': posts,
         # 'form': form,
         # 'anchor': anchor,
    })


def new_thread(request, section_id):  # used
    """Создаёт новую тему."""
    path = request.build_absolute_uri()
    # login_url = settings.LOGIN_URL
    # register_url = reverse('registration_register')
    # if not request.user.is_authenticated():
    #     messages.warning(request, ('Чтобы создать тему, необходимо '
    #                                '<a href="%s">войти</a> или '
    #                                '<a href="%s">зарегистрироваться</a>.') %
    #                      (login_url, register_url))
    #     return redirect_to_login(path, login_url, REDIRECT_FIELD_NAME)

    form = ThreadForm(None)

    if request.POST:
        form = ThreadForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.comments_allowed = True
            thread.section_id = section_id
            thread.user = request.user
            thread.save()
            return redirect(thread)

    section = Section.objects.get(id=section_id)
    return render(request, 'forum/new_thread.html', {
        'form': form,
        'section_id': section_id,
        'section': section
    })


def new_thread_page(request):  # used
    """Отображает страницу создания темы."""
    form = ThreadPageForm()
    return render(request, 'forum/new_thread_page.html', {'form': form})


def subscribe_thread(request):
    pass


def unsubscribe_thread(request):
    pass


class ThreadsListView(ListView):  # used
    """Отображает список тем."""
    context_object_name = 'threads'
    template_name = 'forum/threads.html'
    paginate_by = 10

    def get_queryset(self):
        return Thread.objects.select_related('section', 'section__category').filter(
            section__category__id=self.kwargs['category_id'],
            section__id=self.kwargs['section_id']
        ).order_by('-last_updated')

    def get_context_data(self, **kwargs):
        """
        Добавляет секцию в контекст.

        Секция не должна быть скрытой (is_hidden), иначе отдается 404.
        """
        context = super(ThreadsListView, self).get_context_data(**kwargs)
        context['section'] = get_object_or_404(
            Section.objects.select_related('category'), id=self.kwargs['section_id'], is_hidden=False)
        return context


class SectionsListView(ListView):  # used
    """Отображает список разделов."""
    context_object_name = 'sections'
    template_name = 'forum/sections.html'
    paginate_by = 10

    def get_queryset(self):
        return Section.objects.select_related('category').filter(
            category__id=self.kwargs['category_id'], is_hidden=False
        ).order_by('sort_key')

    def get_context_data(self, **kwargs):
        """
        Добавляет категорию в контекст.

        Категория не должна быть скрытой (is_hidden), иначе отдается 404.
        """
        context = super(SectionsListView, self).get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, id=self.kwargs['category_id'], is_hidden=False)
        return context


def edit_post(request):
    pass


def new_complaint(request):
    pass


def delete_multiple_posts(request):
    pass


def quick_search(request):
    pass


def category_info(request):  # used
    """Возвращает json-данные с разделами выбранной категории."""
    cat_id = request.GET.get('id', None)

    if cat_id is None:
        return HttpResponseBadRequest()
    try:
        cat_id = int(cat_id)
    except ValueError:
        return HttpResponseBadRequest()
    sections = list(Section.objects.filter(category_id=cat_id).values('id', 'name'))

    if not sections:
        return HttpResponseNotFound()
    return HttpResponse(json.dumps(sections), content_type='application/json; charset=UTF-8')


def get_threads_json(request):
    pass

