# Generated by Django 4.2.11 on 2024-04-16 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userlibrary'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userlibrary',
            options={'verbose_name_plural': 'UserLibraries'},
        ),
    ]