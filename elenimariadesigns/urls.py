from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),

    path('posts/', views.post_detail, name='post_detail'),

    path('posts/new', views.post_form, name='post_form'),

    path('posts/<int:pk>', views.post_view, name="post_view"),

    path('posts/<int:pk>/edit', views.post_edit, name='post_edit'),

    path('posts/<int:pk>/delete', views.post_delete, name='post_delete'),

    path('posts/comments/new', views.comment_create, name='comment_create'),

    path('comments', views.comment_list, name='comment_list'),

    path('comment/<int:pk>', views.comment_view, name="comment_view"),

    path('comment/<int:pk>', views.comment_detail, name="comment_detail"),

    path('comment/edit/<int:pk>', views.comment_edit, name='comment_edit'),
    
    path('comments/<int:pk>/delete', views.comment_delete, name='comment_delete')
]
