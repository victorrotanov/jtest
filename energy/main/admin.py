from django.contrib import admin
from django.urls import reverse
from django.shortcuts import redirect
from .models import *


admin.site.site_header = "Панель управления сайтом"
admin.site.site_title = "Управление контентом"
admin.site.index_title = "Добро пожаловать в админку"

admin.site.register(FAQ)
admin.site.register(IndividualAttachment)
admin.site.register(EntityAttachment)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("created_at", "title")
    search_fields = ("title",)
    ordering = ("-created_at",)


@admin.register(Managment)
class ManagmentAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "phone", "email", "hierarchy")
    search_fields = ("name", "position")
    list_filter = ("position","name")
    ordering = ("hierarchy",)

@admin.register(QuestionThemes)
class QuestionThemesAdmin(admin.ModelAdmin):
    list_display = ("name","eMail")
    search_fields = ("name",)
    ordering = ("name",)
    
@admin.register(QuestionMessage)
class QuestionMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "theme", "created_at")
    search_fields = ("name", "email", "phone")
    ordering = ("-created_at",)
    list_filter = ("theme",)

class OrganizationContactAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not OrganizationContact.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        obj = OrganizationContact.objects.first()
        if obj:
            return self.change_view(request, object_id=str(obj.pk))
        return super().changelist_view(request, extra_context)

admin.site.register(OrganizationContact, OrganizationContactAdmin)

class PersonalReceptionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not PersonalReception.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        obj = PersonalReception.objects.first()
        if obj:
            return self.change_view(request, object_id=str(obj.pk))
        return super().changelist_view(request, extra_context)

admin.site.register(PersonalReception, PersonalReceptionAdmin)

class EmergencyServiceAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return EmergencyService.objects.count() == 0

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        obj = EmergencyService.objects.first()
        if obj:
            return self.change_view(request, object_id=str(obj.pk))
        return super().changelist_view(request, extra_context)

admin.site.register(EmergencyService, EmergencyServiceAdmin)

class MetersReadingServiceAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return MeterReadingBaseContacts.objects.count() == 0

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        obj = MeterReadingBaseContacts.objects.first()
        if obj:
            return self.change_view(request, object_id=str(obj.pk))
        return super().changelist_view(request, extra_context)

admin.site.register(MeterReadingBaseContacts, MetersReadingServiceAdmin)
admin.site.register(Streets)
admin.site.register(MeterReadingBoxes)
admin.site.register(Contacts)
admin.site.register(OurProfessionals)
admin.site.register(PublicServicePoint)
admin.site.register(Rates)
admin.site.register(AdditionalInformation)
admin.site.register(Outages)
admin.site.register(Techspec)