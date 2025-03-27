from django.contrib import admin
from django.urls import reverse
from django.shortcuts import redirect
from .models import News, OrganizationContact, Managment


class SingletonModelAdmin(admin.ModelAdmin):
    change_form_template = "admin/change_form.html"

    def get_model_perms(self, request):
        return {"change": True, "view": True}

    def has_add_permission(self, request):
        return not OrganizationContact.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


    def get_queryset(self, request):
        obj = OrganizationContact.objects.first()
        return OrganizationContact.objects.filter(id=obj.id) if obj else OrganizationContact.objects.none()

    def changelist_view(self, request, extra_context=None):
        obj = OrganizationContact.objects.first()
        if obj:
            return redirect(reverse("admin:main_organizationcontact_change", args=[obj.id]))
        return super().changelist_view(request, extra_context)


admin.site.register(OrganizationContact, SingletonModelAdmin)
admin.site.register(News)
admin.site.register(Managment)

admin.site.site_header = "Панель управления сайтом"
admin.site.site_title = "Управление контентом"
admin.site.index_title = "Добро пожаловать в админку"
