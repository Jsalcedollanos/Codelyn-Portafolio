# Generated by Django 4.1.5 on 2023-02-20 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0036_clases_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clases',
            name='url',
            field=models.URLField(blank=True, default='https//:#', max_length=300, null=True, verbose_name='url video'),
        ),
    ]