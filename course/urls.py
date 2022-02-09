from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('unenrolled/<int:c_id>', views.unenrolled, name="unenrolled"),
    path('watched/<str:c_id>/<int:index>', views.watched, name='watched'),
    path('upload', views.upload, name='upload'),
    path('enroll/<int:c_id>', views.enroll, name='enroll'),
]