from django.db import models


class Participant(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10)
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50)
    question_1 = models.CharField(max_length=50, blank=True, null=True)
    question_2 = models.CharField(max_length=50, blank=True, null=True)
    question_3 = models.CharField(max_length=50, blank=True, null=True)
    question_4 = models.CharField(max_length=50, blank=True, null=True)
    question_5 = models.CharField(max_length=50, blank=True, null=True)
    question_6 = models.CharField(max_length=50, blank=True, null=True)
    question_7 = models.CharField(max_length=50, blank=True, null=True)
    question_8 = models.CharField(max_length=50, blank=True, null=True)
    arrival_date = models.DateField(blank=True, null=True)
    spouse_name = models.CharField(max_length=50, blank=True, null=True)
    additional_message = models.TextField(blank=True, null=True)
    gen7_total_attendees = models.IntegerField(default=0, blank=True, null=True)
    payment_reference = models.CharField(max_length=50, blank=True, null=True)
    paid = models.BooleanField(default=False)


class Child(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='children')
    name = models.CharField(max_length=50)
    age = models.IntegerField(blank=True, null=True)


class Donation(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    reference = models.CharField(max_length=50, blank=True, null=True)
    project = models.CharField(max_length=50, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
