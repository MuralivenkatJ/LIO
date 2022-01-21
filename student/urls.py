from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login1"),
    path('logout/', views.logout, name="logout1"),
    path('register/', views.register, name="register1"),
]