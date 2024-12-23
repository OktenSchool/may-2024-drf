from django.urls import path
from .views import UserListCreateView
urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_list_create'),
]