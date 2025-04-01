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
    
class FAQ(models.Model):
    question = models.TextField(verbose_name="Вопрос")
    answer = models.TextField(verbose_name="Ответ")
    hierarchy = models.IntegerField(verbose_name="Иерархия", unique=True)

    class Meta:
        verbose_name = "Вопрос-ответ"
        verbose_name_plural = "Часто задаваемые вопросы"

    def __str__(self):
        return self.question
    
class QuestionThemes(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="Тема вопроса")
    
    class Meta:
        verbose_name = "Тема вопроса"
        verbose_name_plural = "Темы вопросов руководителю"
        
    def __str__(self):
        return self.name

class QuestionMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ваше имя")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    address = models.TextField(max_length=500, verbose_name="Адрес")
    theme = models.ForeignKey(QuestionThemes, on_delete=models.SET_NULL, null=True, verbose_name="Тема вопроса")
    message = models.TextField(verbose_name="Вопрос")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата отправки")
    
    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы руководителю"

    def __str__(self):
        return f"{self.name} ({self.theme})"
    
class PersonalReception(models.Model):
    
    person = models.ForeignKey(Managment, on_delete=models.CASCADE, null=True, verbose_name="Личный прием ведет")
    
    def __str__(self):
        return f"Личный прием: {self.person}" if self.person else "Личный прием (не указан)"
    
    class Meta:
        verbose_name = "Личный прием"
        verbose_name_plural = "Личный прием"
        
class EmergencyService(models.Model):
    
    phone = models.CharField(max_length=100, verbose_name="Телефон")
    whatsapp = models.CharField(max_length=100, verbose_name="WhatsApp")
    
    def __str__(self):
        return f"Аварийная служба: {self.phone}" if self.phone else "Аварийная служба (не задано)"
    
    class Meta:
        verbose_name = "Аварийная служба"
        verbose_name_plural = "Аварийная служба"