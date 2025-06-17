from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse_lazy
import yaml
from pathlib import Path
from .forms import ContactForm
from .models import ContactMessage


def index(request):
    """Homepage view."""
    return render(request, "index.html")


def about(request):
    """About page view."""
    return render(request, "about.html")


def logout_view(request: HttpRequest) -> HttpResponseRedirect:
    """Log out the user and redirect to home."""
    logout(request)
    return HttpResponseRedirect("/")


def modules(request):
    """Display list of project modules."""
    modules = [
        {"name": "Akademik", "icon": "fa-graduation-cap", "slug": "akademik"},
        {"name": "Asrama", "icon": "fa-building", "slug": "asrama"},
        {"name": "Keuangan", "icon": "fa-money-bill-wave", "slug": "keuangan"},
        {"name": "Perpustakaan", "icon": "fa-book", "slug": "perpustakaan"},
        {"name": "HRD", "icon": "fa-users", "slug": "hrd"},
        {"name": "Inventori", "icon": "fa-boxes-stacked", "slug": "inventori"},
    ]
    context = {"modules": modules}
    return render(request, "modules.html", context)


def module_detail(request, slug: str):
    """Placeholder module detail page."""
    modules = {
        "akademik": "Akademik",
        "asrama": "Asrama",
        "keuangan": "Keuangan",
        "perpustakaan": "Perpustakaan",
        "hrd": "HRD",
        "inventori": "Inventori",
    }
    name = modules.get(slug)
    if not name:
        from django.http import Http404

        raise Http404("Module not found")
    context = {"module_name": name}
    return render(request, "module_detail.html", context)


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
            ContactMessage.objects.create(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                message=form.cleaned_data["message"],
            )
            messages.success(request, "Thank you for reaching out!")
            form = ContactForm()
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})
