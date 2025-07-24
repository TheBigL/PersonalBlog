from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Member

class MemberCreationForm(UserCreationForm):
    



    class Meta:
        model = Member
        fields = [ 'username', 'email', 'password1', 'password2' ]

    def save(self, commit=True):
        member = super().save(commit=False)
        member.set_password(self.cleaned_data["password1"])

        if commit:
            member.save()

        return member
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if not username or not password:
            raise forms.ValidationError("Both fields are required.")

        return cleaned_data