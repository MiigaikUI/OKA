from django.shortcuts import render
from django.views import View
from .models import About


class MapView(View):
    def get(self, request):
        return render(request, 'mapFrame.html', {"title": "Map"})


class AboutView(View):
    def get(self, request):
        print(About.get_current())
        return render(request, 'about.html', {"title": "About", "html": About.get_current()})
