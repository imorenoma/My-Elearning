# Generated by Django 3.2.23 on 2024-02-01 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myWeb', '0004_rename_usuario_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
