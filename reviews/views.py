# reviews/views.py
from django.shortcuts import render, get_object_or_404
from .models import Book, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required


@login_required
def user_profile(request):
    return render(request, 'users/profile.html', {'user': request.user})


def book_list(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'reviews/book_list.html', {'books': books})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)  # Fetch the book by ID
    reviews = Review.objects.filter(book=book)  # Fetch reviews for the book

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            return redirect('book_detail', book_id=book.id)
    else:
        form = ReviewForm()

    return render(request, 'reviews/book_detail.html', {'book': book, 'reviews': reviews, 'form': form})