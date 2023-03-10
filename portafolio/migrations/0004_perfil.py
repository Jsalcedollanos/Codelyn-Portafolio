# Generated by Django 3.2.13 on 2023-01-29 15:32

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0003_proyect_progress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre Completo')),
                ('surname', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('title', models.CharField(max_length=50, verbose_name='Titulo')),
                ('email', models.EmailField(max_length=100, verbose_name='Correo')),
                ('telephone', models.IntegerField(max_length=12)),
                ('description', ckeditor.fields.RichTextField(verbose_name='Descripcion')),
                ('skills', models.TextField(max_length=255, verbose_name='Habilidades')),
                ('image', models.ImageField(upload_to='perfil', verbose_name='Imagen perfil')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='fecha creacion')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='fecha actualizacion')),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfiles',
            },
        ),
    ]
