# Generated by Django 5.1.3 on 2024-11-28 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='notified_reset',
            field=models.BooleanField(default=False),
        ),
    ]
