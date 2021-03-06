# Generated by Django 2.1.5 on 2021-01-22 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titulum')),
                ('subtitle', models.CharField(max_length=200, verbose_name='Subtitulum')),
                ('content', models.TextField(verbose_name='Contenitum')),
                ('image', models.ImageField(upload_to='services', verbose_name='Imagenum')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacionum')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edicionum')),
            ],
            options={
                'verbose_name': 'Serviciorum',
                'verbose_name_plural': 'Serviciorummis',
                'ordering': ['-created'],
            },
        ),
    ]
