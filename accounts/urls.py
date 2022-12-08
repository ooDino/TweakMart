from django.urls import path
from .views import RegisterView
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm
from django.views.generic import TemplateView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("member/home", TemplateView.as_view(template_name="OU/memberhome.html"), name="memberhome"),
    path("login/", LoginView.as_view(authentication_form = CustomLoginForm), name="login"),
]