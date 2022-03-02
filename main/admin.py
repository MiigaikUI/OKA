from django.contrib import admin
from .models import Contact, About, Partners


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('status',)

@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ('name',)


# Register your models here.
