from django import forms
from recommand.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # 유저에게 입력받은 field만
        fields = ["comment"]
