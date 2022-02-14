from django.contrib import admin
from .models import Contact, About



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(About)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('status',)


# Register your models here.
