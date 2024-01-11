from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'registered', 'intermediate_access', 'advanced_access')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'level')


class LessonAdmin(admin.ModelAdmin):
    list_display = ('lesson_number', 'course', 'title', 'lesson_type', 'video_source')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
