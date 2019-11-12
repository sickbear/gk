# coding=utf-8
from django.urls import path
from . import views


urlpatterns = [
    path('', views.CategoriesListView.as_view(), name='forum_categories'),  # used
    path('<category_id>/<section_id>/<pk>/', views.thread, name='forum_thread'),  # used
    path('<category_id>/<section_id>/', views.ThreadsListView.as_view(), name='forum_threads'),  # used
    path('<category_id>/', views.SectionsListView.as_view(), name='forum_sections'),  # used
    path('newthread/<section_id>/', views.new_thread, name='forum_new_thread'),
    path('newthreadpage/', views.new_thread_page, name='forum_new_thread_page'),
    path('subscribe/<thread_id>/', views.subscribe_thread, name='forum_subscribe_thread'),
    path('unsubscribe/<thread_id>/', views.unsubscribe_thread, name='forum_unsubscribe_thread'),
    path('editpost/<post_id>/', views.edit_post, name='forum_edit_post'),
    path('complain/', views.new_complaint, name='forum_new_complaint'),
    path('deletemultipleposts/', views.delete_multiple_posts, name='forum_delete_multiple_posts'),
    path('quicksearch/', views.quick_search, name='forum_quick_search'),
    path('categoryinfo/', views.category_info, name='category_info'),
    path('api/threads.json', views.get_threads_json, name='get_threads_json'),
]
