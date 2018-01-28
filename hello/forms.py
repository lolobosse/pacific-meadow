from django import forms

class Contact(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' : 'w-100'}))
    email = forms.EmailField(label="Votre adresse e-mail", widget=forms.TextInput(attrs={'class' : 'w-100'}))
