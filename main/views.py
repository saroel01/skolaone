from django.shortcuts import render


def index(request):
    """Homepage view."""
    return render(request, "index.html")


def about(request):
    """About page view."""
    return render(request, "about.html")


def modules(request):
    """Display list of project modules."""
    module_list = [
        "Akademik",
        "Asrama",
        "Keuangan",
        "Perpustakaan",
        "HRD",
        "Inventori",
    ]
    context = {"modules": module_list}
    return render(request, "modules.html", context)
