from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *

def book_list(request):
    books = Book.objects.all()
    paginator = Paginator(books, 10)
    page = request.GET.get('page')
    books = paginator.get_page(page)
    return render(request, 'book_list.html', {'books': books})

def home(request):
    return render(request, 'home.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})