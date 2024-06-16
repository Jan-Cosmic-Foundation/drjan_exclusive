# Generated by Django 5.0.1 on 2024-06-16 13:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_donation_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='participant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='registration.participant'),
        ),
    ]
