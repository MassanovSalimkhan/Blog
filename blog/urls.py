from django.urls import path
from .views import PostList, PostDetail, PostNew, PostDelete, PostEdit

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('post/new/', PostNew.as_view(), name='post_new'),
    path('post/<int:pk>/delete', PostDelete.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
]