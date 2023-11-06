from django import forms

class UsuarioForm(forms.Form):
    nombre      = forms.CharField(max_length=30)
    rut         = forms.CharField(max_length=9)
    email       = forms.CharField(max_length=35)
    direccion   = forms.CharField(max_length=50)
    username    = forms.CharField(max_length=25)
    password    = forms.CharField(max_length=25)
    rol         = forms.IntegerField()