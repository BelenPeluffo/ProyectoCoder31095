from django.urls import path
from AppCoder.models import Curso
from AppCoder.views import curso

urlpatterns = [
    path('curso/', curso),
]