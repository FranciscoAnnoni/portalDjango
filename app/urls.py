from django.urls import path

# mis vistas
from app.views import plantillaBody
from app.views import tabla
from app.views import list_programmers

urlpatterns = [
    path("", plantillaBody),
    path("tabla/", tabla),
    path("list_programmers/", list_programmers)
]
