from django import forms
class CommentForm(forms.Form):
    name = forms.CharField(max_length=100,label="name:")
    text = forms.CharField(widget=forms.Textarea,label="comment:")