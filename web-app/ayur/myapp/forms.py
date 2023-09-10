# myapp/forms.py

from django import forms

class UserSymptomsForm(forms.Form):
    userData = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your symptoms...'}))
