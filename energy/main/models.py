from django.db import models


class News(models.Model):

    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title


class OrganizationContact(models.Model):
    name = models.CharField(
        max_length=255, verbose_name="Название организации")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    address = models.TextField(verbose_name="Адрес", blank=True, null=True)
    other = models.TextField(
        verbose_name="Другая информация", blank=True, null=True)

    def __str__(self):
        return "Реквизиты организации"

    class Meta:
        verbose_name = "Реквизиты организации"
        verbose_name_plural = "Реквизиты организации"

    def save(self, *args, **kwargs):
        self.__class__.objects.exclude(id=self.id).delete()
        super().save(*args, **kwargs)


class Managment(models.Model):
    hierarchy = models.IntegerField(verbose_name="Иерархия", unique=True)
    name = models.CharField(max_length=255, verbose_name="ФИО")
    position = models.CharField(max_length=255, verbose_name="Должность")
    phone = models.CharField(
        max_length=20, verbose_name="Телефон", blank=True, null=True)
    email = models.EmailField(verbose_name="Email", blank=True, null=True)
    organization = models.ForeignKey(
        OrganizationContact, on_delete=models.CASCADE, verbose_name="Организация", related_name="managment"
    )

    class Meta:
        verbose_name = "Руководство"
        verbose_name_plural = "Руководство"
        ordering = ["hierarchy"]

    def __str__(self):
        return self.name
