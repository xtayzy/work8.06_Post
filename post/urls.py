from django.urls import path

from post import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/info/<int:id>', views.post_info, name='post_info'),
    path('post/delete/<int:id>', views.post_delete, name='post_delete'),
    path('comment/delete/<int:id>', views.comment_delete, name='comment_delete'),
    path('post/edit/<int:id>', views.edit_post, name='edit_post'),
    path('cat/info/<int:id>', views.cat_info, name='cat_info'),
    path('cat/delete/<int:id>', views.cat_delete, name='cat_delete'),
    path('cat/add', views.add_cat, name='add_cat'),
]