# Generated by Django 3.2.23 on 2024-02-02 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myWeb', '0018_remove_user_confirmpassword'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user',
        ),
    ]