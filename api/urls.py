from django.urls import path
from .views import *

urlpatterns = [
    path('autores/', AutoresView.as_view()),
    path('autores/<int:pk>', AutoresRetriveUpdateDestroy.as_view())
]

