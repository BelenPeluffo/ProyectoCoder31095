from django.urls import path
from AppCoder.models import Curso
from AppCoder.views import curso, inicio

urlpatterns = [
    path('', inicio),
    path('curso/', curso, name="AppCoderCurso"),
]