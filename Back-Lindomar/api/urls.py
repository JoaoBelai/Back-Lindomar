from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Your API Title",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@yourapi.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    #swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),

    #GENÉRICOS
    #path('autores', AutoresView.as_view()),
    #path('livros', LivrosView.as_view()),
    #path('editoras', EditorasView.as_view()),
    #path('autores/<int:pk>', AutoresRetriveUpdateDestroy.as_view())

    #AUTORES
    path('autores/', get_autores),
    path('autores/<int:pk>', get_autor),
    path('autores/post', post_autores),
    path('autores/put/<int:pk>', put_autor),
    path('autores/delete/<int:pk>', delete_autor),

    #EDITORAS
    path('editoras/', get_editoras),
    path('editoras/<int:pk>', get_editora),
    path('editoras/post', post_editoras),
    path('editoras/put/<int:pk>', put_editora),
    path('editoras/delete/<int:pk>', delete_editora),

    #LIVROS
    path('livros/', get_livros),
    path('livros/<int:pk>', get_livro),
    path('livros/post', post_livros),
    path('livros/put/<int:pk>', put_livro),
    path('livros/delete/<int:pk>', delete_livro),

    #TOKEN
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

