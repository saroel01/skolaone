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
