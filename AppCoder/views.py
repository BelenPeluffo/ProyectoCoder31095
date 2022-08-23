from django.shortcuts import render
from AppCoder.models import Curso

def curso(request):
    #asignar por keyword, porque si no por POSICIÓN
    #nos pide un ID y tira error:
    curso1=Curso(nombre="Python",camada=31095)
    #para guardar en la DB:
    curso1.save()
    contexto= {
        'curso':curso1,
    }

    return render(request,'template_0.html',contexto)
