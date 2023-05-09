# Generated by Django 4.1.6 on 2023-05-08 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.CharField(max_length=1)),
                ('seat', models.PositiveSmallIntegerField()),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]