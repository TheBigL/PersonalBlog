from django import forms
from .models import Post
from django.contrib.auth import get_user_model

class PostForm(forms.ModelForm):
    title = forms.CharField(label="Title", max_length=150)
    content = forms.CharField(widget=forms.Textarea)

    User = get_user_model()
    
    class Meta:
        model = Post
        fields = ('title', 'content')

'''
    def save(self, commit=True, user=None):
        if user.is_con
'''         