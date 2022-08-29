from django.shortcuts import render, redirect
from AppCoder.forms import CursoFormulario
from AppCoder.models import Curso, Entregable

def curso(request):
    #asignar por keyword, porque si no por POSICIÓN
    #nos pide un ID y tira error:
    curso1=Curso(nombre="Python",camada=31095)
    #para guardar en la DB:
    curso1.save()
    contexto= {
        'curso':curso1,
    }

    #return render(request,'AppCoder/template_0.html',contexto)
    #COMENTO EL ANTERIOR PARA QUE ME ANTE CON EL NUEVO
    return render(request,'AppCoder/otro_y_listo.html',contexto)

def entregable(request):
    entregable1=Entregable(nombre="Mi Primer MVT",fecha_de_entrega="2022-08-24",entregado=True)
    #para guardar en la DB:
    entregable1.save()
    contexto= {
        'entregable':entregable1,
    }

    return render(request,'AppCoder/entregable.html',contexto)

def inicio(request):
    return render(request,'index.html')

def curso_formulario(request):
    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST)
        if mi_formulario.is_valid():
            data=mi_formulario.cleaned_data
            curso1= Curso(nombre=data.get('nombre'),camada=data.get('camada'))
            curso1.save()

            return redirect('AppCoderInicio')
    contexto={
        'form':CursoFormulario()
    }
    return render(request,"AppCoder/curso_formulario.html",contexto)