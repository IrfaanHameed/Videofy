# urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('upload/', views.upload_video, name='upload_video'),
    path('', views.video_list, name='video_list'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('edit/<int:id>/', views.edit_video, name='edit_video'),
    path('delete/<int:id>/', views.delete_video, name='delete_video'),
]

