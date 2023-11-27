from django.urls import path
from .views import EventosViewSet

from django.conf import settings
from rest_framework import routers
from django.conf.urls.static import static
router = routers.DefaultRouter()
router.register('eventos', EventosViewSet)

urlpatterns = [
    #path("ListaEventos/", EventosLista.as_view()),
    #path("<int:id>/", DetallesEventos),
    #path("", CrearEventos),

]

# Para mostrar las imágenes
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 