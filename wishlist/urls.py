from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist, name="wishlist"),
    path('addtowishlist/<int:c_id>', views.add, name='wish'),
    path('deletefromwishlist/<int:c_id>', views.delete, name='delete'),
]