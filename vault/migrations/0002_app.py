# Generated by Django 4.2.11 on 2024-05-05 20:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vault', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('apptype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vault.apptype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
