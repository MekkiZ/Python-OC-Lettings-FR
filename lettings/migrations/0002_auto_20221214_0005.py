# Generated by Django 4.1.4 on 2022-12-14 00:05

from django.db import migrations
# from oc_lettings_site.models import Letting, Address
from lettings.models import Address as new_address, Letting as new_letting


def migrate_data(apps, schema_editor):
    for addresses in Address.objects.all():
        new_addresses = new_address()
        new_addresses.id = addresses.id
        new_addresses.number = addresses.number
        new_addresses.street = addresses.street
        new_addresses.city = addresses.city
        new_addresses.state = addresses.state
        new_addresses.zip_code = addresses.zip_code
        new_addresses.country_iso_code = addresses.country_iso_code

        new_addresses.save()
    for lettings in Letting.objects.all():
        let = new_letting()
        let.title = lettings.title
        let.address = new_address.objects.get(id=lettings.id)
        let.save()


class Migration(migrations.Migration):
    dependencies = [
        ('lettings', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(migrate_data),
    ]