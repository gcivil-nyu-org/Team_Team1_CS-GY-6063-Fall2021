from django import forms
from forum.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)
        widgets = {
            "content": forms.Textarea(attrs={"class": "form-control"}),
        }
