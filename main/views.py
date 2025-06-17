from django.shortcuts import render
from django.contrib import messages
import yaml
from pathlib import Path
from .forms import ContactForm


def index(request):
    """Homepage view."""
    return render(request, "index.html")


def about(request):
    """About page view."""
    return render(request, "about.html")


def modules(request):
    """Display list of project modules."""
    modules = [
        {"name": "Akademik", "icon": "fa-graduation-cap"},
        {"name": "Asrama", "icon": "fa-building"},
        {"name": "Keuangan", "icon": "fa-money-bill-wave"},
        {"name": "Perpustakaan", "icon": "fa-book"},
        {"name": "HRD", "icon": "fa-users"},
        {"name": "Inventori", "icon": "fa-boxes-stacked"},
    ]
    context = {"modules": modules}
    return render(request, "modules.html", context)


def roadmap(request):
    """Display project roadmap from YAML file."""
    roadmap_file = Path(__file__).resolve().parent.parent / "docs" / "roadmap.yaml"
    try:
        with open(roadmap_file, "r", encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
    except FileNotFoundError:
        data = {"phases": []}
    context = {"phases": data.get("phases", [])}
    return render(request, "roadmap.html", context)


def contact(request):
    """Display contact form and handle submissions."""
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, "Thank you for reaching out!")
            form = ContactForm()
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})
