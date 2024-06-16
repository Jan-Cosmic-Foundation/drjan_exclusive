from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Model for user profiles: user, bio, profile pic
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=20, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    registered = models.BooleanField(default=False)
    intermediate_access = models.BooleanField(default=False)
    advanced_access = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Course(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    mini_description = models.CharField(max_length=150)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='course_images')
    level = models.CharField(max_length=50)
    core = models.BooleanField(default=False)
    course_number = models.IntegerField(unique=True, blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return self.title


# class Enrollment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')
#     course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'{self.user} - {self.course}'


class Lesson(models.Model):
    TYPE_CHOICES = (
        ('lesson', 'Lesson'),
        ('supplementary', 'supplementary'),
        ('q&a', 'Q&A'),
    )
    lesson_number = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField()
    lesson_type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='lesson')
    thumbnail = models.ImageField(upload_to='lesson_thumbnails')
    video_source = models.CharField(max_length=50, choices=(('youtube', 'Y'), ('vimeo', 'V')))
    video_id = models.CharField(max_length=100)
    twi_video_id = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title


# class AccessCode(models.Model):
#     """
#     Model for access codes to courses: unique 5-digit code; can access one or more courses
#     """
#     code = models.CharField(max_length=5, unique=True)
#     courses = models.ManyToManyField(Course)
#
#     def __str__(self):
#         return self.code


class Payment(models.Model):
    """
    Model for payments: user, main, amount, date
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.amount} - {self.date}'
    
    
class Comment(models.Model):
    name = models.CharField(max_length=155)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return f'{self.name} - Comment'