# Generated by Django 5.1 on 2024-10-25 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_remove_member_is_contributor'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='is_contributor',
            field=models.BooleanField(default=False),
        ),
    ]
