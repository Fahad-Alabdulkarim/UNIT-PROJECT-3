# Generated by Django 5.1.3 on 2024-12-02 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0008_alter_groupexpense_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='group_type',
        ),
    ]