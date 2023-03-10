# Generated by Django 4.1.5 on 2023-02-20 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0025_alter_contenido_curso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='titulo')),
                ('description', models.TextField(max_length=400, verbose_name='descripcion')),
                ('status', models.BooleanField(default=True, verbose_name='estado')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='fecha creacion')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='fecha actualizacion')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='portafolio.contenido', verbose_name='contenido')),
            ],
        ),
    ]
