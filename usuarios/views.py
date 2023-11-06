from django.shortcuts import render
from .models import Usuario
from .serializers import UsuariosSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

#def inicio(request):
#    context={}
#    return render(request, 'productos/index.html',context)

@api_view(["GET"])
def ListarUsuarios(request):
    usuarios =Usuario.objects.all()
    serializer = UsuariosSerializer(usuarios, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def FiltrarUsuario(request, pk):
    usuarios = Usuario.objects.get(id_usuario=pk)
    serializer = UsuariosSerializer(usuarios, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def CrearUsuario(request):
    serializer = UsuariosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)


@api_view(['POST'])
def ActualizarUsuario(request, pk):
    usuarios = Usuario.objects.get(id_usuario=pk)
    serializer = UsuariosSerializer(instance=usuarios, data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)


@api_view(['DELETE'])
def EliminarUsuario(request, pk):
    usuarios = Usuario.objects.get(id_usuario=pk)
    usuarios.delete()

    return Response('Usuario eliminado')