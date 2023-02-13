from django import forms

class MarkdownForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={"name":"Title"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"name":"Content"}))


class EditForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={"name":"Content"}))