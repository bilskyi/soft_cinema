# Generated by Django 4.1.6 on 2023-06-27 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0008_hall_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seat',
            name='hall',
        ),
        migrations.AddField(
            model_name='seat',
            name='hall',
            field=models.ManyToManyField(to='theater.hall'),
        ),
    ]