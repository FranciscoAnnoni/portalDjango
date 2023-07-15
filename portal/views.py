
from django.http import HttpResponse

#Esto carga las plantillas
from django.template import loader

#En este caso cargo y traigo los datos estaticos de la tabla


# Request: Para realizar peticiones
# HttpResponse: Para enviar la respuesta usando el protocolo HTTP


# Esto es la plantilla de la vista del fondo (Todo lo seteado anteriormetne por nosotros para metrogas)
"""
def plantillaBody(request):
    # Abrimos el documento que tiene la plantilla
    plantillaExterna = open("C:/Users/franc/Desktop/DjangoPortal/portal/portal/plantillas/body.html")
    # Cargar el documento en una variable del tipo Template
    template = Template(plantillaExterna.read())
    # Cerrar la plantilla habierta
    plantillaExterna.close() 
    # Crear un contexto
    contexto = Context()
    # Renderizar el documento
    documento = template.render(contexto)
    return HttpResponse(documento)
"""

# Esto es la plantilla de la vista del fondo (Todo lo seteado anteriormetne por nosotros para metrogas)
def plantillaBody(request):
    plantillaExterna = loader.get_template("body.html")
    documento = plantillaExterna.render()
    return HttpResponse(documento)

def tabla(request):
    plantillaExterna = loader.get_template("tabla.html")
    documento = plantillaExterna.render()
    return HttpResponse(documento)

