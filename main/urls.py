from django.urls import path
from main import views

urlpatterns = [
    path('', views.MapView.as_view(), name="map"),
]
