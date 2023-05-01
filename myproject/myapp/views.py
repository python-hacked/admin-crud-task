from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Book

def book_list(request):
    books = Book.objects.all()
    paginator = Paginator(books, 10)
    page = request.GET.get('page')
    books = paginator.get_page(page)
    return render(request, 'book_list.html', {'books': books})
