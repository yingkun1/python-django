from django import forms
# from .models import User
from django.contrib.auth import get_user_model

class LoginForm(forms.ModelForm):
    remeber = forms.IntegerField(required=False)           #可传可不传
    telephone = forms.CharField(max_length=11)
    class Meta:
        model = get_user_model()
        fields = ['password']