# Generated by Django 3.1.1 on 2020-09-21 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blendApi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='render',
            old_name='date',
            new_name='reqDate',
        ),
    ]
