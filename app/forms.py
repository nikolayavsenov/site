from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    """Класс формы комментария"""
    class Meta:
        model=Comment
        fields=(
            'text',
        )
