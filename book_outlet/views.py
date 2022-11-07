from django.shortcuts import get_object_or_404, render
from .models import Book
from django.http import Http404
from django.db.models import Avg

# Create your views here.


def index(request):
    book = Book.objects.all().order_by("-rating")
    total_number_of_books = book.count()
    average_rating = book.aggregate(Avg("rating"))
    return render(request, "book_outlet/index.html", {"books": book, "total_number_of_books": total_number_of_books, "average_rating": average_rating})


def book_details(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book_details.html",
                  {"title": book.title,
                   "rating": book.rating,
                   "author": book.author,
                   "is_bestselling": book.is_bestselling})
