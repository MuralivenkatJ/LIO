from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('unenrolled/<int:c_id>', views.unenrolled, name="unenrolled"),
    path('enrolled/<str:c_id>/', views.enrolled, name="enrolled"),
    path('upload', views.upload, name='upload'),
    path('wish/<int:c_id>', views.wish, name='wish'),
    path('enroll/<int:c_id>', views.enroll, name='enroll'),
]