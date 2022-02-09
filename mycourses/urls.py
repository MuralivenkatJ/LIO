from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mycourses, name='mycourses'),
    path('reviews/<int:c_id>', views.reviews, name='reviews'),
    path('enrolled/<str:c_id>/', views.enrolled, name="enrolled"),
]