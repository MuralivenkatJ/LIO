from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('unenrolled/', views.unenrolled, name="unenrolled"),
    path('enrolled/<str:playlistid>/', views.enrolled, name="enrolled"),
]