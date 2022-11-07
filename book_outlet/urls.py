from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="book-hp"),
    path('<slug:slug>', views.book_details, name="book-details")
]
