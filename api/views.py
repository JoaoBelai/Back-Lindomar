from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Autor
from .serializers import AutorSerializers

class AutoresView(ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializers

#Faz a mesma coisa do de cima, mas em método é mais manual, não genérico
@api_view(['GET', 'POST'])
def listar_autores(request):
    if request.method == 'GET':
        queryset = Autor.objects.all()
        serializer = AutorSerializers(queryset, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = AutorSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AutoresRetriveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializers