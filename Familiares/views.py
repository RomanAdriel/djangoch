from django.http import HttpResponse
from django.shortcuts import render

from Familiares.models import Familia


def carga_familiares(self):
    familiares = [["Juana", "De Arco", 98, "Madre", "1904-12-25"], ["Cid", "Campeador", 98, "Padre", "1904-12-25"],
                  ["María", "la del Barrio", 98, "Hermana", "1904-12-25"],
                  ["Juana", "De Arco", 98, "Hermana", "1904-12-25"],
                  ["Marcelo", "Tinelli", 78, "Tío", "1914-12-25"], ["Juana", "De Arco", 98, "Prima", "1925-12-25"]]

    for familiar in familiares:
        miembro = Familia(nombre=familiar[0], apellido=familiar[1], edad=familiar[2], parentesco=familiar[3],
                          fecha_nacimiento=familiar[4])
        miembro.save()

    return HttpResponse("Familiares cargados!")


def mostrar_familiares(request):

    lista_familiares = Familia.objects.all()

    context = {'lista_familiares': lista_familiares}

    return render(request, 'familiares.html', context)