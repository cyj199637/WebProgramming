from django.shortcuts import render, get_object_or_404
from .models import Book

# Create your views here.
def BookListView(request):
    books = Book.objects.all()

    return render(request, 'book_list.html', {'books': books})



def BookDetailView(request, code):
    book1 = get_object_or_404(Book, code=code)
    book2 = Book.objects.get(code=code)

    return render(request, 'book_detail.html', {'book': book2})