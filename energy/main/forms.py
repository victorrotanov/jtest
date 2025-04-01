from django import forms
from .models import QuestionMessage
from django_recaptcha.fields import ReCaptchaField

class QuestionMessageForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = QuestionMessage
        fields = ['name', 'email', 'phone', 'address', 'theme', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'theme': forms.Select(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
        