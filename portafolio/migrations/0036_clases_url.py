# Generated by Django 4.1.5 on 2023-02-20 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0035_alter_clases_title_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='clases',
            name='url',
            field=models.URLField(blank=True, default='https//:#', max_length=300, verbose_name='url video'),
        ),
    ]
