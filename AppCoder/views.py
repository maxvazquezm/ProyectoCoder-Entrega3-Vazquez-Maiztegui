from django.shortcuts import render
from .models import Curso

from .forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario
from .models import Curso,Profesor,Estudiante
# Create your views here.


from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView



def inicio_view(request):
    return render(request, "AppCoder/inicio.html")


def cursos_view(request):
    if request.method == "GET":
        print("+" * 90) #  Imprimimos esto para ver por consola
        print("+" * 90) #  Imprimimos esto para ver por consola
        return render(
            request,
            "AppCoder/curso_formulario_avanzado.html",
            {"form": CursoFormulario()}
        )
    else:
        print("*" * 90)     #  Imprimimos esto para ver por consola
        print(request.POST) #  Imprimimos esto para ver por consola
        print("*" * 90)     #  Imprimimos esto para ver por consola

        modelo = Curso(curso=request.POST["curso"], camada=request.POST["camada"])
        modelo.save()
        return render(
            request,
            "AppCoder/inicio.html",
        )


def profesor_view(request):
    if request.method == "GET":
        return render(
            request,
            "AppCoder/profesor_formulario_avanzado.html",
            {"form": ProfesorFormulario()}
        )
    else:
        formulario = ProfesorFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            modelo = Profesor(
                nombre=informacion["nombre"],
                apellido=informacion["apellido"],
                email=informacion["email"],
                profesion=informacion["profesion"]
            )
            modelo.save()
        return render(
            request,
            "AppCoder/inicio.html",
        )
    
def estudiante_view(request):
    if request.method == "GET":
        return render(
            request,
            "AppCoder/estudiante_formulario_avanzado.html",
            {"form": EstudianteFormulario()}
        )
    else:
        formulario = EstudianteFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            modelo = Estudiante(
                nombre=informacion["nombre"],
                apellido=informacion["apellido"],
                email=informacion["email"],
            )
            modelo.save()
        return render(
            request,
            "AppCoder/inicio.html",
        )
    
def cursos_crud_read_view(request):
    cursos = Curso.objects.all()
    return render(request, "AppCoder/cursos_lista.html", {"cursos": cursos})

def estudiantes_crud_read_view(request):
    estudiantes = Estudiante.objects.all()
    return render(request, "AppCoder/estudiantes_lista.html", {"estudiantes": estudiantes})


def profesores_crud_read_view(request):
    profesores = Profesor.objects.all()
    return render(request, "AppCoder/profesores_lista.html", {"profesores": profesores})


def profesores_crud_delete_view(request, profesor_email):
    profesor_a_eliminar = Profesor.objects.filter(email=profesor_email).first()
    profesor_a_eliminar.delete()
    return profesores_crud_read_view(request)


def profesores_crud_update_view(request, profesor_email):
    profesor = Profesor.objects.filter(email=profesor_email).first()
    if request.method == "GET":
        formulario = ProfesorFormulario(
            initial={
                "nombre": profesor.nombre,
                "apellido": profesor.apellido,
                "email": profesor.email,
                "profesion": profesor.profesion
            }
        )
        return render(request, "AppCoder/profesores_formulario_edicion.html", {"form": formulario, "profesor": profesor})
    else:
        formulario = ProfesorFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            profesor.nombre=informacion["nombre"]
            profesor.apellido=informacion["apellido"]
            profesor.email=informacion["email"]
            profesor.profesion=informacion["profesion"]
            profesor.save()
        return profesores_crud_read_view(request)



