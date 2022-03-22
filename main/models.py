from django.db import models


class Contact(models.Model):
    first_name = models.CharField(
        "Имя",
        max_length=32,
        help_text="Имя участника",
        blank=True,
    )
    last_name = models.CharField(
        "Фамилия",
        max_length=32,
        help_text="Фамилия участника",
        blank=True,
    )
    img = models.ImageField(
        "Фото",
        upload_to="contact/",
        help_text="Фото участника",
        blank=True,
        default='contact/default.jpg'
    )
    role = models.TextField(
        "Роль",
        max_length=4096,
        help_text="Роль участника в проекте",
        blank=True,
    )
    description = models.CharField(
        "Описание",
        max_length=256,
        help_text="Описание участника",
        blank=True,
    )

    @classmethod
    def get_current(cls):
        member_left = []
        member_right = []
        for index, member in enumerate(cls.objects.all()):
            print(member)
            if index % 2 == 0:
                member_left.append(member)
            else:
                member_right.append(member)
        return member_left, member_right

    class Meta():
        verbose_name_plural = "Команда"
        verbose_name = "Участника"

class Partners(models.Model):
    name = models.CharField(
        "Название",
        max_length=256,
        help_text="Название партнёра",
        blank=False,
    )

    img = models.ImageField(
        "Фото",
        upload_to="partners/",
        help_text="Фото партнёра",
        blank=False,
        default='partners/default.jpg'
    )
    url = models.URLField(
        "Ссылка",
        max_length=256,
        help_text="Описание участника",
        blank=False,
    )

    @classmethod
    def get_current(cls):
        partners_left = []
        partners_right = []
        for index, partner in enumerate(cls.objects.all()):
            print(partner)
            if index % 2 == 0:
                partners_left.append(partner)
            else:
                partners_right.append(partner)
        return partners_left, partners_right

    class Meta():
        verbose_name_plural = "Партнёры"
        verbose_name = "Партнёра"


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
        result = cls.objects.all().filter(status=1)
        return result.first().html

    class Meta():
        verbose_name_plural = "описания 'О проекте'"
        verbose_name = "О проекте"
