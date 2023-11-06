from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
from rest_framework.utils import json
from .forms import UsuarioForm
from django.views.decorators.csrf import csrf_protect


# Create your views here.


def index(request):
    response = requests.get('http://127.0.0.1:8000/usuarios/').json()
    return render(request, 'web/index.html', {
        'response': response
    })


@csrf_protect
def post_usuario(request):
    url = "http://127.0.0.1:8000/usuarios/crear"
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        rut         = form.cleaned_data.get("rut")
        nombre      = form.cleaned_data.get("nombre")
        email       = form.cleaned_data.get("email")
        direccion   = form.cleaned_data.get("direccion")
        username    = form.cleaned_data.get("username")
        password    = form.cleaned_data.get("password")
        rol         = form.cleaned_data.get("rol")
        
        data = {'rut': rut, 'nombre': nombre, 'email': email, 'direccion': direccion, 'username': username, 'password': password, 'rol': rol}
        
        headers = {'Content-type': 'application/json', }
        response = requests.post(url, data=json.dumps(data), headers=headers)
        return render(request, 'web/form.html', {
            'response': response
        })