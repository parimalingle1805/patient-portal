# Generated by Django 5.1.2 on 2024-11-11 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_portal_app', '0010_appointments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='user_appointment',
            field=models.DateTimeField(max_length=50),
        ),
    ]