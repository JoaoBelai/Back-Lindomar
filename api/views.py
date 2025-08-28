from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Autor, Editora, Livro
from .serializers import AutorSerializers, EditoraSerializers, LivroSerializers

# class AutoresView(ListCreateAPIView):
#     queryset = Autor.objects.all()
#     serializer_class = AutorSerializers

# class EditorasView(ListCreateAPIView):
#     queryset = Editora.objects.all()
#     serializer_class = EditoraSerializers

# class LivrosView(ListCreateAPIView):
#     queryset = Livro.objects.all()
#     serializer_class = LivroSerializers

# class AutoresRetriveUpdateDestroy(RetrieveUpdateDestroyAPIView):
#     queryset = Autor.objects.all()
#     serializer_class = AutorSerializers

#Faz a mesma coisa do de cima, mas em método é mais manual, não genérico
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_autores(request):
    queryset = Autor.objects.all()
    serializer = AutorSerializers(queryset, many = True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_autor(request, pk):
    queryset = Autor.objects.get(pk=pk)
    serializer = AutorSerializers(queryset)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_editoras(request):
    queryset = Editora.objects.all()
    serializer = EditoraSerializers(queryset, many = True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_editora(request, pk):
    queryset = Editora.objects.get(pk=pk)
    serializer = EditoraSerializers(queryset)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_livros(request):
    queryset = Livro.objects.all()
    serializer = LivroSerializers(queryset, many = True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_livro(request, pk):
    queryset = Livro.objects.get(pk=pk)
    serializer = LivroSerializers(queryset)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def post_autores(request):
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
        
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def post_editoras(request):
    if request.method == 'GET':
        queryset = Editora.objects.all()
        serializer = EditoraSerializers(queryset, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = EditoraSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def post_livros(request):
    if request.method == 'GET':
        queryset = Livro.objects.all()
        serializer = LivroSerializers(queryset, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LivroSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def put_autor(request, pk):
    if request.method == 'GET':
        queryset = Autor.objects.get(pk=pk)
        serializer = AutorSerializers(queryset)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        try:
            autor = Autor.objects.get(pk=pk)
        except Autor.DoesNotExist:
            return Response({'error' : 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AutorSerializers(autor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def put_livro(request, pk):
    if request.method == 'GET':
        queryset = Livro.objects.get(pk=pk)
        serializer = LivroSerializers(queryset)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        try:
            livro  = Livro.objects.get(pk=pk)
        except Livro.DoesNotExist:
            return Response({'erro' : 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = LivroSerializers(livro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def put_editora(request, pk):
    if request.method == 'GET':
        queryset = Editora.objects.get(pk=pk)
        serirializer = EditoraSerializers(queryset)
        return Response(serirializer.data)
    
    elif request.method == 'PUT':
        try:
            editora = Editora.objects.get(pk=pk) 
        except Editora.DoesNotExist:
            return Response({'erro': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serirializer = EditoraSerializers(editora, data=request.data)
        if serirializer.is_valid():
            serirializer.save()
            return Response(serirializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serirializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def delete_autor(request, pk):
    if request.method == 'GET':
        queryset = Autor.objects.get(pk=pk)
        serializer = AutorSerializers(queryset)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        try:
            autor = Autor.objects.get(pk=pk) 
        except Autor.DoesNotExist:
            return Response({'erro': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        
        autor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def delete_livro(request, pk):
    if request.method == 'GET':
        queryset = Livro.objects.get(pk=pk)
        serializer = LivroSerializers(queryset)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        try: 
            livro = Livro.objects.get(pk=pk)
        except Livro.DoesNotExist:
            return Response({'erro', 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        
        livro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def delete_editora(request, pk):
    if request.method == 'GET':
        queryset = Editora.objects.get(pk=pk)
        serializer = EditoraSerializers(queryset)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        try: 
            editora = Editora.objects.get(pk=pk)
        except Editora.DoesNotExist:
            return Response({'erro': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        
        editora.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
