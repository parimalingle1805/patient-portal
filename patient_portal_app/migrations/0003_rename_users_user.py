# Generated by Django 5.1.1 on 2024-10-19 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient_portal_app', '0002_alter_users_user_phone'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]
