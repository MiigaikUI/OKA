# Generated by Django 4.0 on 2022-02-14 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_partners'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partners',
            name='name',
            field=models.CharField(help_text='Название партнёра', max_length=256, verbose_name='Название'),
        ),
    ]
