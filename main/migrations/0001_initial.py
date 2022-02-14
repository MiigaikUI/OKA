# Generated by Django 4.0 on 2022-02-14 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('html', models.CharField(max_length=4096, verbose_name="Содержание страници 'О проекте' ")),
            ],
            options={
                'verbose_name': 'О проекте',
                'verbose_name_plural': "описания 'О проекте'",
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Имя участника', max_length=32, verbose_name='Имя')),
                ('last_name', models.CharField(help_text='Фамилия участника', max_length=32, verbose_name='Фамилия')),
                ('img', models.ImageField(blank=True, help_text='Фото участника', upload_to='contact/', verbose_name='Фото')),
                ('role', models.CharField(help_text='Роль участника в проекте', max_length=64, verbose_name='Роль')),
                ('description', models.CharField(help_text='Описание участника', max_length=256, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Участник',
                'verbose_name_plural': 'Команда',
            },
        ),
    ]