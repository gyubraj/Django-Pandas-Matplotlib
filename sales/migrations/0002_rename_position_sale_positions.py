# Generated by Django 3.2.3 on 2021-05-14 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='position',
            new_name='positions',
        ),
    ]
