# Generated by Django 4.1.6 on 2023-06-29 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(unique=True)),
                ('is_available', models.BooleanField(default=True)),
                ('hall', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='theater.hall')),
            ],
            options={
                'ordering': ['number'],
            },
        ),
    ]
