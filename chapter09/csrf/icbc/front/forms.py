from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    password_repeat = forms.CharField(max_length=20)

    def clean(self):
        cleaned_date = super().clean()
        password = cleaned_date.get('password')
        password_repeat = cleaned_date.get('password_repeat')
        if password   != password_repeat:
            raise forms.ValidationError("两次输入的密码不一致!  ")
        return cleaned_date

    class Meta:
        model = User
        fields = ['username','password','email']

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','password']

class TransferForm(forms.Form):
    email = forms.EmailField(max_length=100)
    money = forms.FloatField()
