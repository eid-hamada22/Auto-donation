# Generated by Django 4.1.5 on 2023-02-24 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_item_alter_donation_type_item_desire_donation_item_c'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery_point',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]