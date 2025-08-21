from django.urls import path
from .views import *

urlpatterns = [
    # path('autores', AutoresView.as_view()),
    #path('livros', LivrosView.as_view()),
    #path('editoras', EditorasView.as_view()),
    #path('autores/<int:pk>', AutoresRetriveUpdateDestroy.as_view())
    path('autores', get_autores),
    path('autores/<int:pk>', get_autor),
    path('autores/post', post_autores),
    path('editoras', get_editoras),
    path('editoras/<int:pk>', get_editora),
    path('editoras/post', post_editoras),
    path('livros', get_livros),
    path('livros/<int:pk>', get_livro),
    path('livros/post', post_livros),
]

