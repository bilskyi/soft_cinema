# Generated by Django 4.1.6 on 2023-05-01 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_category_options_remove_movie_cat_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='movie',
            name='released',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.PositiveIntegerField(),
        ),
        migrations.AddField(
            model_name='movie',
            name='state',
            field=models.ManyToManyField(to='home.state'),
        ),
    ]
