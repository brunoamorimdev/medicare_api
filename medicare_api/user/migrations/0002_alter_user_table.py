# Generated by Django 4.2.6 on 2023-10-28 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='auth_user',
        ),
    ]
