# Generated by Django 5.0.1 on 2024-04-23 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_donation'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='additional_message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='question_8',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]