# Generated by Django 5.1.5 on 2025-04-01 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_emergencyservice_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emergencyservice',
            name='phone',
            field=models.CharField(max_length=100, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='emergencyservice',
            name='whatsapp',
            field=models.CharField(max_length=100, verbose_name='WhatsApp'),
        ),
    ]
