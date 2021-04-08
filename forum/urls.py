from django.urls import path

from . import views

app_name = "forum"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('thread/<int:pk>', views.ThreadView.as_view(), name='thread'),
    path('threadS/<int:pk>', views.ThreadViewSecure.as_view(), name='threadS'),
    path('newThread', views.newThread, name='newThread'),
    path('newPost', views.newPost, name='newPost'),
    path('likePost', views.likePost, name='likePost'),
    ]
