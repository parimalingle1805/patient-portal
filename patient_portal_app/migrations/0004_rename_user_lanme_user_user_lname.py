# Generated by Django 5.1.1 on 2024-10-19 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient_portal_app', '0003_rename_users_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_lanme',
            new_name='user_lname',
        ),
    ]
