# Generated by Django 4.0.3 on 2022-03-06 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('book_details', models.CharField(max_length=150)),
                ('book_author', models.CharField(max_length=100)),
                ('book_image', models.ImageField(upload_to='bookpics')),
                ('book_path', models.FileField(upload_to='bookpath')),
            ],
        ),
    ]
