from .models import Comment
from django import forms
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['name','email','commentDes']
        labels={
            'commentDes':'Comment Description'
        }