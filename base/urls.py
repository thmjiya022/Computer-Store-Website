from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('logout/', views.login_page, name='logout'),
    path('register/', views.register_user, name='register'),

    path('', views.home, name='home')
]