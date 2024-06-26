# Generated by Django 4.2.11 on 2024-05-18 11:55

from django.db import migrations
import uuid

def gen_uuid(apps, schema_editor):
    User = apps.get_model("users", "User")
    for row in User.objects.all():
        row.verification_code = uuid.uuid4()
        row.save(update_fields=["verification_code"])

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_verification_code'),
    ]

    operations = [
        migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
    ]
