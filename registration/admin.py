from django.contrib import admin
from .models import Participant, Child, Donation
# Register your models here.


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    search_fields = ('first_name', 'last_name', 'email', 'phone')


class ChildAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')
    search_fields = ('name', 'age')


class DonationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'reference', 'amount', 'paid')
    search_fields = ('name', 'email', 'reference', 'amount', 'paid')


admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Child, ChildAdmin)
admin.site.register(Donation, DonationAdmin)
