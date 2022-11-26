from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('register/', views.registration, name='registration'),
    path('login/', views.loginPage, name='loginPage'),
    path('logout/', views.logoutUser, name='logout'),
]