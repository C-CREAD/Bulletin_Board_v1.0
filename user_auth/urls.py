from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'user_auth'
urlpatterns = [
    path('', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('authenticate_user/', views.authenticate_user,
         name='authenticate_user'),
    path('show_user/', views.show_user, name='show_user'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='authentication/logout.html'), name='logout'),
]
