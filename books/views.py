# books/views.py
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from .models import Book
from django.db.models import Q

class BookListView(LoginRequiredMixin,ListView):
    model = Book
    context_object_name = "book_list" 
    template_name = "books/book_list.html"
    login_url = "account_login"

class BookDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView): 
    model = Book
    context_object_name = "book"
    template_name = "books/book_detail.html"
    login_url = "account_login"
    permission_required = "books.special_status"  # nouveau

class SearchResultsListView(ListView):  # nouveau
    model = Book
    context_object_name = "book_list"
    template_name = "books/search_results.html"
    
    def get_queryset(self):  # Nouveau
        query = self.request.GET.get("q")  # Récupère "q" depuis l'URL
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)  # Filtre titre OU auteur
        )