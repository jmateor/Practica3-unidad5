from django.contrib import admin
from .models import Maestro, Materia, Estudiante, Inscripcion, Nota, Asistencia

admin.site.register(Maestro)
admin.site.register(Materia)
admin.site.register(Estudiante)
admin.site.register(Inscripcion)
admin.site.register(Nota)
admin.site.register(Asistencia)