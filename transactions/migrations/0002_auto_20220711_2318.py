# Generated by Django 3.2.9 on 2022-07-10 11:29
import json
from django.db import migrations


def create_base_transactions(apps, schema_editor):
    file = open('base_transactions.json')
    data = json.load(file)
    transaction = apps.get_model('transactions', 'TransactionType')
    for trans in data:
        transaction.objects.create(**trans)


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_base_transactions)
    ]