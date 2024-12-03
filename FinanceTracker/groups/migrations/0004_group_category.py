# Generated by Django 5.1.3 on 2024-11-30 16:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0001_initial'),
        ('groups', '0003_groupinvitation_groupmembership'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='finances.category'),
        ),
    ]