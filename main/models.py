from django.db import models


class Contact(models.Model):
    first_name = models.CharField(
        "Имя",
        max_length=32,
        help_text="Имя участника",
        blank=False,
    )
    last_name = models.CharField(
        "Фамилия",
        max_length=32,
        help_text="Фамилия участника",
        blank=False,
    )
    img = models.ImageField(
        "Фото",
        upload_to="contact/",
        help_text="Фото участника",
        blank=True,
    )
    role = models.CharField(
        "Роль",
        max_length=64,
        help_text="Роль участника в проекте",
        blank=False,
    )
    description = models.CharField(
        "Описание",
        max_length=256,
        help_text="Описание участника",
        blank=False,
    )

    class Meta():
        verbose_name_plural = "Команда"
        verbose_name = "Участник"


class About(models.Model):
    status = models.BooleanField(
        "Активность",
        help_text="Оставьте только одно единственное активный объект для отображения желаемого контента",
    )
    html = models.TextField(
        "Содержание страницы ",
        max_length=8192
    )

    @classmethod
    def get_current(cls):
        result = cls.objects.filter(status=True)
        return result.values()[0]['html']

    class Meta():
        verbose_name_plural = "описания 'О проекте'"
        verbose_name = "О проекте"
