# Generated by Django 4.2.11 on 2024-04-19 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_userlibrary_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='stripe_account_id',
            field=models.CharField(default='123', max_length=100),
            preserve_default=False,
        ),
    ]
