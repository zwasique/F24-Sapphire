# Generated by Django 5.1.2 on 2024-10-30 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="inbox",
            options={"verbose_name_plural": "Inboxes"},
        ),
        migrations.AddField(
            model_name="user",
            name="biography",
            field=models.CharField(default="Hello, world!", max_length=1000),
        ),
    ]
