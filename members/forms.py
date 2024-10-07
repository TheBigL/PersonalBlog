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