from django.contrib import admin
from .models import Participant, Child
# Register your models here.


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    search_fields = ('first_name', 'last_name', 'email', 'phone')


class ChildAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')
    search_fields = ('name', 'age')


admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Child, ChildAdmin)
