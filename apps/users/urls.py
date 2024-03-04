from django.urls import path

from apps.users.views import UserAPIView, PostAPIView

urlpatterns = [
    path('users/<pk>', UserAPIView.as_view(), name='user-delete'),
    path('users/', UserAPIView.as_view(), name='users'),
    path('posts/', PostAPIView.as_view(), name='posts'),

]
