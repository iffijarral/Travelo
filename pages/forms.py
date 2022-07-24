from email import message
from django import forms

class ContactForm(forms.Form):
    yourname = forms.CharField(max_length=100, label="Your name")
    email = forms.CharField(required=False, max_length=100, label="Your email")
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)