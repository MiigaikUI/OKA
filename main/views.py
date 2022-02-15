from django.shortcuts import render
from django.views import View
from .models import About, Contact, Partners


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
        return render(request, 'team.html', {"title": "Team", "members_left": members[0], "members_right": members[1]})


class PartnersView(View):
    def get(self, request):
        partners = Partners.get_current()
        print(partners)
        return render(request, 'partners.html', {"title": "Partners", "partners_left": partners[0], "partners_right": partners[1]})
