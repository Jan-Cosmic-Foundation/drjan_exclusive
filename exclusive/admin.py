from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'phone_number', 'registered', 'intermediate_access', 'advanced_access')
    actions = ['make_registered', 'make_intermediate', 'make_advanced']

    def make_registered(self, request, queryset):
        queryset.update(registered=True)

    make_registered.short_description = "Mark selected profiles as registered"

    def make_intermediate(self, request, queryset):
        queryset.update(intermediate_access=True)

    make_intermediate.short_description = "Mark selected profiles as intermediate"

    def make_advanced(self, request, queryset):
        queryset.update(advanced_access=True)

    make_advanced.short_description = "Mark selected profiles as advanced"


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'mini_description', 'level')
    prepopulated_fields = {'slug': ('title',)}


class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'lesson_number', 'course', 'title', 'lesson_type', 'video_source')
    prepopulated_fields = {'slug': ('title',)}
    
    
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "amount", "date")
    

class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email")


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Comment, CommentAdmin)
