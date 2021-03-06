# coding=utf-8
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from material.admin.sites import site
from gorodkirov.users import views as user_views
from gorodkirov.articles import views as article_views
from . import views

app_name = 'gorodkirov'
site.site_header = settings.ADMIN_TITLE

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', user_views.register, name='register'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', include('gorodkirov.users.urls')),
    path('activate/<uidb64>/<token>/', user_views.activate, name='activate'),
    path('admin/', include('material.admin.urls')),
    path('content/', include('gorodkirov.articles.urls')),
    path('news/', article_views.timeline, name='timeline'),
    path('tags/', article_views.articles_by_tags, name='articles_by_tags'),
    path('forum/', include('gorodkirov.forum.urls')),
    path('search/', views.search, name='search'),

    path('accounts/', include('allauth.urls')),
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls)), ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
