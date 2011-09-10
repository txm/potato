from django.forms import ModelForm
from django import forms

from txm.models import Blog


class BlogForm(ModelForm):
        
    body = forms.CharField(widget=forms.Textarea) 

    class Meta:
        model = Blog
        #exclude = ['date']

