from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'type' : 'text', 
            'required' : 'required',
        })
        
        self.fields["email"].widget.attrs.update({
            'type' : 'email', 
            'required' : 'required',
        })

        self.fields["password1"].widget.attrs.update({
            'type' : 'password', 
            'required' : 'required',
        })

        self.fields["password2"].widget.attrs.update({
            'type' : 'password', 
            'required' : 'required',
        })
        

class CustomLoginForm(AuthenticationForm):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['username'].widget.attrs.update({ 
      'type': 'username',
      'required': 'required',
    })
    self.fields['password'].widget.attrs.update({
      'type': 'password',
      'required': 'required',
    })
