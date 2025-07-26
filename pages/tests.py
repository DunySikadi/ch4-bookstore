# pages/tests.py
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView  # nouveau

class HomepageTests(SimpleTestCase):
    def setUp(self):  # nouveau
        url = reverse("home")
        self.response = self.client.get(url)
        
    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_homepage_template(self):  # nouveau
        self.assertTemplateUsed(self.response, "home.html")
    
    def test_homepage_contains_correct_html(self):  # nouveau
        self.assertContains(self.response, "home page")

    def test_homepage_does_not_contain_incorrect_html(self):  # nouveau
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")
        
    def test_homepage_url_resolves_homepageview(self):  # nouveau
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)