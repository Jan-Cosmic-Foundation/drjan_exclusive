from django.contrib import admin
from .models import Participant, Child, Donation
# Register your models here.


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'question_3', 'country')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    list_filter = ('question_3', 'country')


class ChildAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')
    search_fields = ('name', 'age')


class DonationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'reference', 'amount', 'project', 'paid')
    search_fields = ('name', 'email', 'reference', 'amount', 'paid')
    list_filter = ('paid',)


admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Child, ChildAdmin)
admin.site.register(Donation, DonationAdmin)
