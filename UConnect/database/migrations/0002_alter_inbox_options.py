# Generated by Django 5.1.2 on 2024-10-30 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("database", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="inbox",
            options={"verbose_name_plural": "Inboxes"},
        ),
    ]
