# Generated by Django 5.1.3 on 2024-12-03 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0011_group_unique_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='unique_code',
        ),
    ]
