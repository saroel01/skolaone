from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import ContactMessage


class SimplePageTests(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_about_page(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "about.html")

    def test_modules_page(self):
        response = self.client.get(reverse("modules"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "modules.html")

    def test_roadmap_page(self):
        response = self.client.get(reverse("roadmap"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "roadmap.html")

    def test_contact_page_get(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact.html")

    def test_contact_form_post(self):
        response = self.client.post(
            reverse("contact"),
            {"name": "Tester", "email": "tester@example.com", "message": "Hi"},
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Thank you for reaching out!")
        self.assertEqual(ContactMessage.objects.count(), 1)

    def test_login_logout_flow(self):
        User.objects.create_user(username="demo", password="secret")
        login_page = self.client.get(reverse("login"))
        self.assertEqual(login_page.status_code, 200)
        self.client.post(reverse("login"), {"username": "demo", "password": "secret"})
        index_after_login = self.client.get(reverse("index"))
        self.assertTrue(index_after_login.context["user"].is_authenticated)
        self.client.get(reverse("logout"))
        after_logout = self.client.get(reverse("index"))
        self.assertFalse(after_logout.context["user"].is_authenticated)

    def test_module_detail_pages(self):
        slugs = [
            "akademik",
            "asrama",
            "keuangan",
            "perpustakaan",
            "hrd",
            "inventori",
        ]
        for slug in slugs:
            resp = self.client.get(reverse("module_detail", args=[slug]))
            self.assertEqual(resp.status_code, 200)

