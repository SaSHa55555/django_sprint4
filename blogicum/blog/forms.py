from django import forms
from django.contrib.auth.models import User

from .models import Post, Comment


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author',)
        widgets = {
            'pub_date': forms.DateTimeInput(attrs={'type': 'datetime-local'},
                                            format='%Y-%m-%dT%H:%M')
        }
        # fields = ['title', 'text', 'pub_date', 'category', 'image',
        # 'location']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
