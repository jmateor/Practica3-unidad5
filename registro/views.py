from django.shortcuts import render
from .models import Estudiante, Inscripcion, Nota
from django.db.models import Avg

def listado_notas(request):
    estudiantes = Estudiante.objects.all()
    datos = []

    for estudiante in estudiantes:
        inscripciones = Inscripcion.objects.filter(estudiante=estudiante)
        for inscripcion in inscripciones:
            notas = Nota.objects.filter(inscripcion=inscripcion)
            promedio = notas.aggregate(Avg('calificacion'))['calificacion__avg'] or 0
            aprobado = promedio >= 70
            datos.append({
                'estudiante': estudiante,
                'materia': inscripcion.materia,
                'promedio': round(promedio, 2),
                'aprobado': aprobado
            })

    return render(request, 'registro/listado_notas.html', {'datos': datos})