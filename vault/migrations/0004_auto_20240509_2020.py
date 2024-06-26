# Generated by Django 4.2.11 on 2024-05-09 18:20

from django.db import migrations


class Migration(migrations.Migration):
    def create_apptype(apps, schema_editor):
        AppType = apps.get_model('vault', 'AppType')
        AppType.objects.create(name="Website")
    
    dependencies = [
        ('vault', '0003_credential'),
    ]

    operations = [
        migrations.RunPython(create_apptype)
    ]
