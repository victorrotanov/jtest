from django.shortcuts import render, redirect
from .models import News, OrganizationContact,Managment, FAQ, PersonalReception, EmergencyService, IndividualAttachment, EntityAttachment
from .forms import QuestionMessageForm
import ssl
import certifi
import os
os.environ['SSL_CERT_FILE'] = certifi.where()

def get_default_context():
    return {
        'organization': OrganizationContact.objects.first(),
        'management': Managment.objects.all(),
        'personal_reception': PersonalReception.objects.first(),
        'emergency_service': EmergencyService.objects.first(),
    }
    
def home(request):
    context = get_default_context()
    context['news'] = News.objects.all()
    return render(request, 'main/main.html', context)

def contacts(request):
    context = get_default_context()
    return render(request, 'main/contacts.html', context)

def history(request):
    context = get_default_context()
    return render(request, 'main/history.html', context)

def managment(request):
    context = get_default_context()
    return render(request, 'main/managment.html', context)

def procurement(request):
    context = get_default_context()
    return render(request, 'main/procurement.html', context)

def strategy(request):
    context = get_default_context()
    return render(request, 'main/strategy.html', context)

def outages(request):
    context = get_default_context()
    return render(request, 'main/outages.html', context)

def investments(request):
    context = get_default_context()
    return render(request, 'main/investments.html', context)

def meter_readings(request):
    context = get_default_context()
    return render(request, 'main/meter_readings.html', context)

def individuals(request):
    context = get_default_context()
    context['attachments'] = IndividualAttachment.objects.all()
    return render(request, 'main/individuals.html', context)

def entities(request):
    context = get_default_context()
    context['attachments'] = EntityAttachment.objects.all()
    return render(request, 'main/entities.html', context)   

def techspec(request):
    context = get_default_context()
    return render(request, 'main/techspec.html', context)

def plunder(request):
    context = get_default_context()
    return render(request, 'main/plunder.html', context)

def esaving(request):
    context = get_default_context()
    return render(request, 'main/esaving.html', context)

def stap(request):
    context = get_default_context()
    return render(request, 'main/stap.html', context)

def points(request):
    context = get_default_context()
    return render(request, 'main/points.html', context)

def payments(request):
    context = get_default_context()
    return render(request, 'main/payments.html', context)

def tariffs(request):
    context = get_default_context()
    return render(request, 'main/tariffs.html', context)

def warmth(request):
    context = get_default_context()
    return render(request, 'main/warmth.html', context)

def question(request):
    context = get_default_context()
    context['faqs'] = FAQ.objects.all().order_by("hierarchy")
    context['form'] = QuestionMessageForm()

    if request.method == "POST":
        form = QuestionMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')

    return render(request, 'main/question.html', context)
    
def success(request):   
    context = get_default_context()
    return render(request, 'main/success_page.html', context)

def training(request):
    context = get_default_context()
    return render(request, 'main/training.html', context)

def ourprofs(request):
    context = get_default_context()
    return render(request, 'main/ourprofs.html', context)

def vacancy(request):
    context = get_default_context()
    return render(request, 'main/vacancy.html', context)

def test(request):
    context = get_default_context()
    return render(request, 'main/test.html', context)

def green(request):
    context = get_default_context()
    return render(request, 'main/green.html', context)

def hrsafety(request):
    context = get_default_context()
    return render(request, 'main/hrsafety.html', context)