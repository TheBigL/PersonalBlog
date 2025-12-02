from django import forms
from .models import Portfolio


class PortfolioForm(forms.ModelForm):
    title = forms.CharField(label="Title", max_length=150)
    content = forms.CharField()
    img = forms.ImageField(label="Portfolio Image", required=False)
    link = forms.URLField(label="Portfolio Link", required=False)

    class Meta:
        model = Portfolio
        fields = ('title', 'content')