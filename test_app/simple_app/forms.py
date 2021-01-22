from django import forms


class SimpleForm(forms.Form):
    ''' form for index view '''
    email = forms.EmailField()
