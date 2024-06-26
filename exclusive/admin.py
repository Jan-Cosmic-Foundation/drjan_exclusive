from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'phone_number', 'registered', 'intermediate_access', 'advanced_access')


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
