from django.conf.urls.static import static
from django.urls import path

from OKA import settings
from main import views

urlpatterns = [
    path('', views.MapView.as_view(), name="map"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('team/', views.TeamView.as_view(), name="team"),
    path('', views.MapView.as_view(), name="partners"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
