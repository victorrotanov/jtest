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
    photo = models.FileField(upload_to='managment/', verbose_name="Фото", blank=True, null=True)
    biography = models.TextField(verbose_name="Биография", blank=True, null=True)
    education = models.TextField(verbose_name="Образование", blank=True, null=True)
    recommendations = models.TextField(verbose_name="Рекомендация", blank=True, null=True)
    birchday = models.DateField(verbose_name="Дата рождения", blank=True, null=True)
    
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
    eMail = models.CharField(max_length=200, null=True, blank=True, verbose_name="Электронная почта")
    
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
    description = models.TextField(verbose_name="Описание")
    
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
        
class IndividualAttachment(models.Model):
    
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    file = models.FileField(upload_to='attachments/', verbose_name="Файл", blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Бытовым потребителям"
        verbose_name_plural = "Бытовым потребителям"

class EntityAttachment(models.Model):
    
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    file = models.FileField(upload_to='attachments/', verbose_name="Файл")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Небытовым потребителям"
        verbose_name_plural = "Небытовым потребителям"
        
class MeterReadingBaseContacts(models.Model):
    whatsapp_entity = models.CharField(max_length=300, verbose_name="Небытовые потребители whatsapp")
    phones_individual = models.CharField(max_length=300, verbose_name="Бытовым потребителям номера телефонов")
    bots = models.CharField(max_length=50, verbose_name="Бытовым потребителям WhatsAppBot, TelegramBot")
    eMail = models.CharField(max_length=100, verbose_name="Бытовым потребителям eMail")
    phones_private = models.CharField(max_length=300, verbose_name="Частный сектор номера телефонов")
    WhatsApp_private = models.CharField(max_length=300, verbose_name="Частный сектор whatsapp")
    appart_WhatsApp = models.CharField(max_length=300, verbose_name="Многоэтажные дома whatsapp или SMS")
    entity_eMail = models.CharField(max_length=100, verbose_name="Небытовым потребителям eMail")

    def __str__(self):
        return self.whatsapp_entity
    
    class Meta:
        verbose_name = "Прием показаний"
        verbose_name_plural = "Прием показаний"
        
class Streets(models.Model):
    streetName = models.CharField(max_length=100, verbose_name="Наименование улицы")
    
    def __str__(self):
        return self.streetName
    
    class Meta:
        verbose_name = "Улица"
        verbose_name_plural = "Улицы"
        
class MeterReadingBoxes(models.Model):
    name = models.CharField(max_length=50, null=False, verbose_name="Наименование")
    street = models.ForeignKey(Streets, on_delete=models.CASCADE, null=False, verbose_name="Улица")
    home = models.CharField(max_length=5, verbose_name="Номер дома")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Ящик для приема показаний"
        verbose_name_plural = "Ящики для приема показаний"
        
class Contacts(models.Model):
    name = models.CharField(max_length=300, null=False, verbose_name="Наименование",unique=True)
    phone = models.TextField(max_length=100, null=True, blank=True, verbose_name="Телефоны")
    eMail = models.CharField(max_length=100, null=True, blank=True, verbose_name="eMail")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        
class OurProfessionals(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name="ФИО")
    description = models.TextField(max_length=2000, null=False, blank=False, verbose_name="Описание")
    photo = models.FileField(upload_to='profs/', verbose_name="Фото", blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Профессионал"
        verbose_name_plural = "Наши профеcсионалы"
        
class PublicServicePoint(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False,verbose_name="Пункт обслуживания населения")
    location = models.CharField(max_length=200, null=False, blank=False,verbose_name="Место расположения")
    workSchedule = models.TextField(max_length=1000, null=False, blank=False, verbose_name="Режим работы")
    services = models.TextField(max_length=1000, null=False, blank=False, verbose_name="Комплекс услуг")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Пункт обслуживания населения"
        verbose_name_plural = "Пункты обслуживания населения"
        
class Rates(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False,verbose_name="Наименование")
    withTax = models.DecimalField(max_length=10, max_digits=10, decimal_places=2, null=False,blank=False,verbose_name="С НДС")
    noTax = models.DecimalField(max_length=10, max_digits=10, decimal_places=2, null=False,blank=False,verbose_name="Без НДС")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Тариф"
        verbose_name_plural = "Тарифы"
    