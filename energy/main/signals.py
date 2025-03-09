from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import OrganizationContact


@receiver(post_migrate)
def ensure_single_contact(sender, **kwargs):
    if not OrganizationContact.objects.exists():
        OrganizationContact.objects.create(
            name="Название компании",
            email="info@example.com",
            phone="+7 777 777 77 77",
            address="Адрес",
        )
