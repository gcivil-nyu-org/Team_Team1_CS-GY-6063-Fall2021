from django import forms
from mptt.forms import TreeNodeChoiceField
from forum.models import Comment


class CommentForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=Comment.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["parent"].widget.attrs.update({"class": "d-none"})
        self.fields["parent"].label = ""
        self.fields["parent"].required = False

    class Meta:
        model = Comment
        fields = (
            "parent",
            "content",
        )
        widgets = {
            "content": forms.Textarea(attrs={"class": "form-control"}),
        }
