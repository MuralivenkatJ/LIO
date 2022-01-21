from django.urls import path
from . import views

urlpatterns = [
    path('', views.explore, name="explore"),
    path('query/', views.query, name="query"),
    path('query1/<str:str>/', views.query1, name="query1"),
]