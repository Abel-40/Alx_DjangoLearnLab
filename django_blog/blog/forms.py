from django import forms
from .models import Profile, Post, Comment
from taggit.forms import TagWidget
from django.forms import widgets
from django.contrib.auth.models import User

# ProfileForm: Used to handle profile updates
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']

# PostForm: Handles post creation and updates
class PostForm(forms.ModelForm):
    title = forms.CharField(widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}))
    author = forms.ModelChoiceField(queryset=User.objects.all(), widget=widgets.Select(attrs={'class': 'form-select', 'placeholder': 'Author'}))
    content = forms.CharField(widget=widgets.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content'}))
    tags = forms.CharField(widget=TagWidget(attrs={'class': 'form-control'}))  # Using TagWidget here for tag handling

    class Meta:
        model = Post
        fields = ['title', 'author', 'content', 'tags']

# CommentForm: Handles comment creation
class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=widgets.Textarea(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Content',
                'style': 'font-size: 12px; padding: 16px; height: 80px;',
            }
        )
    )

    class Meta:
        model = Comment
        fields = ['content']
