from django.urls import path
from .views import RegisterView, PrivacyView, EditUserView, EditPassword
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("member/home", TemplateView.as_view(template_name="OU/memberhome.html"), name="memberhome"),
    path("login/", LoginView.as_view(authentication_form = CustomLoginForm), name="login"),
    path("profile/", TemplateView.as_view(template_name="OU/memberprofile.html"), name="memberprofile"),
    path("profile/payment&wallet", TemplateView.as_view(template_name="OU/memberpaymentandwallet.html"), name="memberpaymentandwallet"),
    path("profile/transaction", TemplateView.as_view(template_name="OU/membertransaction.html"), name="membertransaction"),
    path("profileupdate/", EditUserView, name="profileupdate",),
    path("profilepasswordupdate/", EditPassword, name="profilepasswordupdate",),
    # path("privacy/", auth_views.PasswordChangeView(template_name="OU/memberprivacy.html", success_url=reverse_lazy("memberprivacy")), name="password_change"),
]