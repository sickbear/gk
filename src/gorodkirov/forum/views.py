# coding=utf-8
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Category, Section, Thread, Post
from .forms import PostForm


class CategoriesListView(ListView):  # used
    """Отображает список категорий."""
    queryset = Category.objects.filter(is_hidden=False).order_by('sort_key')
    context_object_name = 'categories'
    template_name = 'forum/categories.html'
    paginate_by = 20


def thread(request, category_id, section_id, pk):  # used
    """Показать тред на форуме."""
    thread = get_object_or_404(Thread.objects.select_related('section', 'section__category'), id=pk)
    posts = thread.posts.all()

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


def new_thread(request):
    pass


def new_thread_page(request):
    pass


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


def category_info(request):
    pass


def get_threads_json(request):
    pass

