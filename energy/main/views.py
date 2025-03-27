from django.shortcuts import render
from .models import News, OrganizationContact,Managment


def home(request):
    news = News.objects.all()
    organization = OrganizationContact.objects.first()
    management = Managment.objects.all()
    return render(request, 'main/main.html', {'news': news, 'organization': organization, 'management': management})

def contacts(request):
    organization = OrganizationContact.objects.first()
    management = Managment.objects.all()
    return render(request, 'main/contacts.html', {'organization': organization, 'management': management})

def history(request):
    organization = OrganizationContact.objects.first()
    management = Managment.objects.all()
    return render(request, 'main/history.html', {'organization': organization, 'management': management})

def managment(request):
    organization = OrganizationContact.objects.first()
    management = Managment.objects.all()
    return render(request, 'main/managment.html', {'organization': organization, 'management': management})

def procurement(request):
    organization = OrganizationContact.objects.first()
    management = Managment.objects.all()
    return render(request, 'main/procurement.html', {'organization': organization, 'management': management})

def strategy(request):
    organization = OrganizationContact.objects.first()
    management = Managment.objects.all()
    return render(request, 'main/strategy.html', {'organization': organization, 'management': management})

def outages(request):
    organization = OrganizationContact.objects.first()
    management = Managment.objects.all()
    return render(request, 'main/outages.html', {'organization': organization, 'management': management})

def evolution(request):
    organization = OrganizationContact.objects.first()
    management = Managment.objects.all()
    return render(request, 'main/evolution.html', {'organization': organization, 'management': management})

def investments(request):
    organization = OrganizationContact.objects.first()
    management = Managment.objects.all()
    return render(request, 'main/investments.html', {'organization': organization, 'management': management})

def meter_readings(request):
    organization = OrganizationContact.objects.first()
    management = Managment.objects.all()
    return render(request, 'main/meter_readings.html', {'organization': organization, 'management': management})

def individuals(request):
    organization = OrganizationContact.objects.first()
    management = Managment.objects.all()
    return render(request, 'main/individuals.html', {'organization': organization, 'management': management})

def entities(request):
    organization = OrganizationContact.objects.first()
    management = Managment.objects.all()
    return render(request, 'main/entities.html', {'organization': organization, 'management': management})

def techspec(request):
    organization = OrganizationContact.objects.first()
    management = Managment.objects.all()
    return render(request, 'main/techspec.html', {'organization': organization, 'management': management})

def plunder(request):
    organization = OrganizationContact.objects.first()
    management = Managment.objects.all()
    return render(request, 'main/plunder.html', {'organization': organization, 'management': management})

def esaving(request):
    organization = OrganizationContact.objects.first()
    management = Managment.objects.all()
    return render(request, 'main/esaving.html', {'organization': organization, 'management': management})

def stap(request):
    organization = OrganizationContact.objects.first()
    management = Managment.objects.all()
    return render(request, 'main/stap.html', {'organization': organization, 'management': management})

def points(request):
    organization = OrganizationContact.objects.first()
    management = Managment.objects.all()
    return render(request, 'main/points.html', {'organization': organization, 'management': management})

def payments(request):
    organization = OrganizationContact.objects.first()
    management = Managment.objects.all()
    return render(request, 'main/payments.html', {'organization': organization, 'management': management})

def tariffs(request):
    organization = OrganizationContact.objects.first()
    management = Managment.objects.all()
    return render(request, 'main/tariffs.html', {'organization': organization, 'management': management})

def warmth(request):
    organization = OrganizationContact.objects.first()
    management = Managment.objects.all()
    return render(request, 'main/warmth.html', {'organization': organization, 'management': management})

def question(request):
    organization = OrganizationContact.objects.first()
    management = Managment.objects.all()
    return render(request, 'main/question.html', {'organization': organization, 'management': management})

def training(request):
    organization = OrganizationContact.objects.first()
    management = Managment.objects.all()
    return render(request, 'main/training.html', {'organization': organization, 'management': management})

def ourprofs(request):
    organization = OrganizationContact.objects.first()
    management = Managment.objects.all()
    return render(request, 'main/ourprofs.html', {'organization': organization, 'management': management})