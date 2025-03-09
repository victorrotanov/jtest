from django.shortcuts import render
from .models import News, OrganizationContact,Managment


def home(request):
    news = News.objects.all()
    organization = OrganizationContact.objects.first()
    management = Managment.objects.all()
    return render(request, 'main/index.html', {'news': news, 'organization': organization, 'management': management})
