from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('modules/', views.modules, name='modules'),
    path('modules/<slug:slug>/', views.module_detail, name='module_detail'),
    path('roadmap/', views.roadmap, name='roadmap'),
    path('contact/', views.contact, name='contact'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
]
