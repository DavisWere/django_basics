from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser, StudentMarks

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name',
                   'email', 'phone_code', 'phone_number',
                   'profile_picture', 'user_type','password']
        

class StudentMakrsForm(forms.ModelForm):
    class Meta:
        model = StudentMarks
        fields = ['database1','database2']

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'px-4 py-2 border-b rounded', 'placeholder': 'Enter your username'})
        self.fields['password'].widget.attrs.update({'class': 'px-4 py-2 border-b rounded', 'placeholder': 'Enter your password'})
