# from django.db import models
#
#
# class Participant(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField()
#     phone = models.CharField(max_length=15)
#     age = models.IntegerField()
#     gender = models.CharField(max_length=10)
#     country = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)
#     question_1 = models.CharField(max_length=50)
#     question_2 = models.CharField(max_length=50)
#     question_3 = models.CharField(max_length=50)
#     question_4 = models.CharField(max_length=50)
#     question_5 = models.CharField(max_length=50)
#     question_6 = models.CharField(max_length=50)
#     question_7 = models.CharField(max_length=50)
#     date_of_arrival = models.DateField()
#
#
# class Gen7Registration(models.Model):
#     participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
#     spouse_name = models.CharField(max_length=50)
#     number_of_children = models.IntegerField()
#
#
# class Child(models.Model):
#     participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#     age = models.IntegerField()
#     t_shirt_size = models.CharField(max_length=10)
#
