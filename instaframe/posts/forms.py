"""Post forms."""

# Django
from django import forms

# models
from .models import Post


class PostForm(forms.ModelForm):
    """Post model form.
    
    Automatic form genetated by django using the post model
    """

    class Meta:
        """Form settings."""
        model = Post
        fields = (
            'user',
            'profile',
            'title',
            'photo'
        )