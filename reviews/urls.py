# reviews/urls.py
from django.urls import path
from .views import book_list, book_detail, user_profile  # Ensure these names match the function names in views.py

urlpatterns = [
    path('', book_list, name='book_list'),
    path('book/<int:book_id>/', book_detail, name='book_detail'),
    path('profile/', user_profile, name='user_profile'),
    path('users/', user_profile, name='user_profile'),  # Add this line for /users
]