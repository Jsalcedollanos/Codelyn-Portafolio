# Generated by Django 4.1.5 on 2023-02-01 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0007_remove_service_offert_remove_service_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='subservices',
            field=models.TextField(default='null', max_length=250, verbose_name='servicios'),
        ),
    ]
