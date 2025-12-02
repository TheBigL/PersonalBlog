from django import forms
from .models import Portfolio


class PortfolioForm(forms.ModelForm):
    title = forms.CharField(label="Title", max_length=150)
    content = forms.CharField()

    class Meta:
        model = Portfolio
        fields = ('title', 'content')