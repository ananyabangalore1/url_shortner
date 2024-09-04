from django import forms

class ShortenURLForm(forms.Form):
    url = forms.URLField(label='Enter your URL', max_length=200, required=True)
    