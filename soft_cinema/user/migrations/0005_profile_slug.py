# Generated by Django 4.1.6 on 2023-06-18 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_profile_managers_remove_profile_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
    ]