from django.shortcuts import render
from datetime import datetime, timedelta
from .models import Book

def books_view(request):
    books = Book.objects.all().order_by('pub_date')
    return render(request, 'books/books_list.html', {'books': books})

def books_by_date(request, pub_date):
    date = datetime.strptime(pub_date, '%Y-%m-%d').date()
    books = Book.objects.filter(pub_date=date)

    # Получение предыдущей и следующей дат
    previous_date = date - timedelta(days=1)
    next_date = date + timedelta(days=1)

    return render(request, 'books/books_by_date.html', {
        'books': books,
        'pub_date': pub_date,
        'previous_date': previous_date,
        'next_date': next_date
    })