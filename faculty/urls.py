from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login2"),
    path('logout/', views.logout, name="logout2"),
    path('register/', views.register, name="register2"),
    path('', views.faculty, name='faculty'),
]