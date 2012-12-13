from django import forms

class BookSuggestionForm(forms.Form):
    title = forms.CharField()
    url = forms.URLField(label='Book URL')
    author = forms.CharField(required=False)
    submitter_name = forms.CharField(required=False, label='Your name')
    submitter_email = forms.EmailField(required=False, label='Your email')
