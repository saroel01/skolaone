from django.test import TestCase
from django.urls import reverse


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
