from django.views.generic import TemplateView
from .views import HomeView
from django.urls import path

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contact/", TemplateView.as_view(template_name="OU/membercontact.html"), name="contact")
]