from django.urls import path
from AppCoder.models import Curso
from AppCoder.views import curso, entregable, inicio, curso_formulario

urlpatterns = [
    path('', inicio, name='AppCoderInicio'),
    path('curso/', curso, name="AppCoderCurso"),
    path('entregable/', entregable, name="AppCoderEntregable"),
    path('curso_formulario/',curso_formulario,name="AppCoderCursoFormulario"),
]