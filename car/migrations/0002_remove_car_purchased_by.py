# Generated by Django 4.2.7 on 2024-01-13 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='purchased_by',
        ),
    ]
