from django.shortcuts import render
from django.views import View

from OKA.settings import MEDIA_URL
from .models import About, Contact


class MapView(View):
    def get(self, request):
        return render(request, 'mapFrame.html', {"title": "Map"})


class AboutView(View):
    def get(self, request):
        print(About.get_current())
        return render(request, 'about.html', {"title": "About", "html": About.get_current()})


class TeamView(View):
    def get(self, request):
        members = Contact.get_current()
        print(members)
        return render(request, 'team.html', {"title": "Team", "members_left": members[0], "members_right": members[1]})
