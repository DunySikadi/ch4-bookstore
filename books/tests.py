# books/tests.py
from django.contrib.auth import get_user_model  # Nouveau
from django.test import TestCase
from django.urls import reverse
from .models import Book, Review  # Nouveau

class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Création d'un utilisateur de test
        cls.user = get_user_model().objects.create_user(
            username="reviewuser",
            email="reviewuser@email.com",
            password="testpass123",
        )
        
        # Création d'un livre de test
        cls.book = Book.objects.create(
            title="Harry Potter",
            author="JK Rowling",
            price="25.00",
        )
        
        # Création d'un avis lié au livre
        cls.review = Review.objects.create(
            book=cls.book,
            author=cls.user,
            review="Un excellent avis",  # Adapté en français
        )

    def test_book_listing(self):
        self.assertEqual(f"{self.book.title}", "Harry Potter")
        self.assertEqual(f"{self.book.author}", "JK Rowling")
        self.assertEqual(f"{self.book.price}", "25.00")

    def test_book_list_view(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Harry Potter")
        self.assertTemplateUsed(response, "books/book_list.html")

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get("/books/12345/")  # URL invalide
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Harry Potter")
        self.assertContains(response, "Un excellent avis")  # Vérification de l'avis
        self.assertTemplateUsed(response, "books/book_detail.html")