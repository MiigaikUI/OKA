from django.conf.urls.static import static
from django.urls import path

from OKA import settings
from main import views

urlpatterns = [
    path('', views.MapView.as_view(), name="map"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
