# Generated by Django 4.2.6 on 2023-11-12 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_managers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'auth user', 'verbose_name_plural': 'auth users'},
        ),
    ]
