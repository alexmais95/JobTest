from django import forms
from django.contrib.auth.models import User



class LogForm(forms.Form):
    username = forms.CharField(max_length=100, label='username' , widget=forms.TextInput(attrs={'class':'log_user'}))
    password = forms.CharField(label='password' , widget=forms.PasswordInput(attrs={'class':'log_user'}))


class RegistForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username',)

    def check_password(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Wrong password')
        return cd['password2']