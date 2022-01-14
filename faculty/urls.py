from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login2"),
    path('register/', views.register, name="register2"),
]