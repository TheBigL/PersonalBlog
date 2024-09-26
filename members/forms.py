from django import forms
from djangon.contrib.auth.forms import UserCreationForm
from models import Member

class MemberCreationForm(UserCreationForm):
    email = forms.EmailField()



    class Meta:
        model = Member
        fields = ['email', 'password', 'password2' ]