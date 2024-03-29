from django.urls import path
from .views import Home, DetailPost, CreatePost, DeletePost, UpdatePost

urlpatterns = [
    path('', Home.as_view(), name='home'),
    # path('mypost/', MyPost.as_view(), name='mypost'),
    path('detail/<int:pk>', DetailPost.as_view(), name='detail'),
    path('detail/<int:pk>/update', UpdatePost.as_view(), name='update'),
    path('detail/<int:pk>/delete', DeletePost.as_view(), name='delete'),
    path('create/', CreatePost.as_view(), name='create'),
]