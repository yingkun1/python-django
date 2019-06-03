from django import forms
from django.core import validators
from .models import User

class BaseForm(forms.Form):
    def get_errors(self):
        errors = self.errors.get_json_data()
        new_errors = {}
        for key,message_lists in errors.items():
            messages = []
            for message_dict in message_lists:
                message = message_dict['message']
                messages.append(message)
            new_errors[key] = messages
        return new_errors

class MyForm(BaseForm):
    # email = forms.EmailField(error_messages={'invalid':'请输入正确的邮箱!'})
    # price =forms.FloatField(error_messages={'invalid':"请输入浮点类型"})
    # personal_website = forms.URLField(error_messages={'invalid':"请输入正确格式的个人网站",'required':'请输入个人网站'})
    # email = forms.CharField(validators=[validators.EmailValidator(message='请输入正确的邮箱')])
    # email = forms.CharField(validators=[validators.EmailValidator(message={'invaild':'请输入正确的邮箱'})])
    # telephone = forms.CharField(validators=[validators.RegexValidator(r'1[345678]\d{9}',message='请输入正确的手机号码!')])
    pass

class RegisterForm(BaseForm):
    username = forms.CharField(max_length=100)
    telephone = forms.CharField(validators=[validators.RegexValidator(r'1[345678]\d{9}',message='请输入正确的手机号码!')])
    pwd1 = forms.CharField(max_length=16,min_length=6)
    pwd2 = forms.CharField(max_length=16,min_length=6)

    def clean_telephone(self):
        telephone = self.cleaned_data.get('telephone')
        exists = User.objects.filter(telephone=telephone).exists()
        if exists:
            raise forms.ValidationError(message="%s:手机号码已经被注册过了,请重新输入!"%telephone)
        else:
            #如果验证没有出现BUG,需要把telephone返回
            return telephone

    #重写clean方法
    #来到了clean方法，那么说明每一个字段都验证成功了
    def clean(self):
        #先调用父类的方法:
        cleaned_data = super().clean()
        pwd1 = cleaned_data.get('pwd1')
        pwd2 = cleaned_data.get('pwd2')
        if pwd1 != pwd2:
            raise forms.ValidationError(message='两次输入密码不一致!')
        else:
            return cleaned_data


