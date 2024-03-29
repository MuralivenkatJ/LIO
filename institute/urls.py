from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register3'),
    path('login/', views.login, name='login3'),
    path('logout/', views.logout, name='logout3'),
    path('approvals/', views.approvals, name='approvals'),
    path('screenshot/<str:id>', views.screenshot, name='screenshot'),
    path('approve/<str:id>', views.approve, name='approve'),
    path('approve2/<str:id>', views.approve2, name='approve2'),
    path('approve3/<str:id>', views.approve3, name='approve3'),
]