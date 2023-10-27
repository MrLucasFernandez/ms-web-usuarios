from django.shortcuts import render
from .models import Usuarios
from .serializers import UsuariosSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

#def inicio(request):
#    context={}
#    return render(request, 'productos/index.html',context)

@api_view(["GET"])
def ListarUsuarios(request):
    usuarios =Usuarios.objects.all()
    serializer = UsuariosSerializer(usuarios, many=True)
    return Response(serializer.data)