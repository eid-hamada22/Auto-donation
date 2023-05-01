# Generated by Django 4.1.5 on 2023-01-28 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0002_beneficiary_entry_date_delivery_point_entry_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery_point',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]