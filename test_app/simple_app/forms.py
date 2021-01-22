from django import forms


class SimpleForm(forms.Form):
    email = forms.EmailField()
