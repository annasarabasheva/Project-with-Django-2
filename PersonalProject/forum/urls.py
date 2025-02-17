from django.urls import path

from PersonalProject.forum import views

urlpatterns = [
    path('category/<int:category_id>/', views.category_view, name='category_view'),
    path('thread/<int:thread_id>/', views.thread_view, name='thread_view'),
    path('thread/<int:thread_id>/post/', views.create_post, name='create_post'),
    path('', views.forum_home, name='forum_home'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),

]