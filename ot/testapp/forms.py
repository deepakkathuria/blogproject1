from django import forms
from testapp.models import Comment

class EmailSendForm(forms.Form):
    name=forms.CharField(max_length=24)
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(required=False,widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','email','body')
