# Generated by Django 4.1.5 on 2023-02-24 13:25

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0039_alter_clases_curso'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='diplomas',
            field=ckeditor.fields.RichTextField(default='null', verbose_name='Diplomas'),
        ),
    ]
