# Generated by Django 5.1.2 on 2024-11-10 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_portal_app', '0005_symptom'),
    ]

    operations = [
        migrations.AddField(
            model_name='symptom',
            name='prescription',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='symptom',
            name='suggestions',
            field=models.CharField(default=None, max_length=50),
        ),
    ]