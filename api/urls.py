from django.urls import path
from .views import *

urlpatterns = [
    # path('autores', AutoresView.as_view()),
    #path('livros', LivrosView.as_view()),
    #path('editoras', EditorasView.as_view()),
    path('autores', listar_criar_autores),
    path('editoras', listar_criar_editoras),
    path('livros', listar_criar_livros),
    path('autores/<int:pk>', AutoresRetriveUpdateDestroy.as_view())
]

