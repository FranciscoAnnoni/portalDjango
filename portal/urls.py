from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls'))
]

"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", plantillaBody),
    path("tabla/", tabla)
]
"""