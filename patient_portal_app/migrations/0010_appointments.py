# Generated by Django 5.1.2 on 2024-11-11 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_portal_app', '0009_alter_symptom_prescription_alter_symptom_suggestions_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_appointment', models.CharField(max_length=50)),
            ],
        ),
    ]
