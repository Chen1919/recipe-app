# Generated by Django 3.2.23 on 2024-01-12 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_recipe_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_acctive',
        ),
    ]
