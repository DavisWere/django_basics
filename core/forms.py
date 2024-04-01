from django import forms
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

    