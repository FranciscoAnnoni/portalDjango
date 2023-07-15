
from django.http import HttpResponse
from django.http.response import JsonResponse
#Esto carga las plantillas
from django.template import loader

#En este caso cargo y traigo los datos estaticos de la tabla
from .models import Programmer


# Esto es la plantilla de la vista del fondo (Todo lo seteado anteriormetne por nosotros para metrogas)
def plantillaBody(request):
    plantillaExterna = loader.get_template("body.html")
    documento = plantillaExterna.render()
    return HttpResponse(documento)

def tabla(request):
    plantillaExterna = loader.get_template("tabla.html")
    documento = plantillaExterna.render()
    return HttpResponse(documento)

# traigo los datos para cargar la tabla
def list_programmers(request):
    programmers = list(Programmer.objects. values())
    data = {'programmers':programmers}
    return JsonResponse(data)
