# Generated by Django 4.2.4 on 2023-08-18 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_yangilikmodels_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yangilikmodels',
            name='User',
        ),
    ]
