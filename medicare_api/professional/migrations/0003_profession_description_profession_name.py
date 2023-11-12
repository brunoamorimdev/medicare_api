# Generated by Django 4.2.6 on 2023-10-31 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professional', '0002_remove_professional_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profession',
            name='description',
            field=models.TextField(blank=True, default='', max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='profession',
            name='name',
            field=models.CharField(blank=True, default='', max_length=80),
        ),
    ]
