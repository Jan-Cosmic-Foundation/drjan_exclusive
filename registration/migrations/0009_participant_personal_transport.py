# Generated by Django 5.0.1 on 2024-11-30 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0008_rename_city_participant_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='personal_transport',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]