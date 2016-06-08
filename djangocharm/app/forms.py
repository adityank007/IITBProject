from django import forms
from .models import UserInfo
from django.contrib.auth.models import User
class UserInfoForm(forms.ModelForm):
	class Meta:
		model = UserInfo
		exclude = ['user']

class UserForm(forms.ModelForm):
    class Meta:
        model = User 
        password = forms.CharField(widget=forms.PasswordInput())
        fields = ['username','password']
        widgets = {
            'password': forms.PasswordInput(),
        }