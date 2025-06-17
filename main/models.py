from django.db import models


class ContactMessage(models.Model):
    """Store contact form submissions."""

    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:  # pragma: no cover - simple representation
        return f"{self.name} <{self.email}>"

