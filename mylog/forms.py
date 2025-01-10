from django import forms

class CreateNewUser(forms.Form):
    name = forms.CharField(label="Ingresa tu nombre",widget=forms.TextInput(attrs={'class' : 'Inputs'}))
    lastname = forms.CharField(label="Ingresa tu apellido", widget=forms.TextInput(attrs={'class' : 'Inputs'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'Inputs'}), label="Ingresa tu contraseña")