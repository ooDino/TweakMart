from django.urls import path
from .views import RegisterView, EditUserView, EditPassword, AddCard, Withdraw, Deposit
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm
from django.views.generic import TemplateView
from django.urls import reverse_lazy

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("member/home", TemplateView.as_view(template_name="OU/memberhome.html"), name="memberhome"),
    path("login/", LoginView.as_view(authentication_form = CustomLoginForm), name="login"),
    path("profile/", TemplateView.as_view(template_name="OU/memberprofile.html"), name="memberprofile"),
    path("profileupdate/", EditUserView, name="profileupdate",),
    path("profilepasswordupdate/", EditPassword, name="profilepasswordupdate",),
    path("wallet/", TemplateView.as_view(template_name="OU/memberpaymentandwallet.html"), name="wallet"),
    path("addcard/", AddCard, name="addcard",),
    path("withdraw/", Withdraw, name="withdraw",),
    path("deposit/", Deposit, name="deposit",),
]