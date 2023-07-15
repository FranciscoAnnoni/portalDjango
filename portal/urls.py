from django.contrib import admin
from django.urls import path

# mis vistas
from portal.views import plantillaBody

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", plantillaBody)
]
