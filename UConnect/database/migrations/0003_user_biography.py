# Generated by Django 5.1.2 on 2024-10-30 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("database", "0002_alter_inbox_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="biography",
            field=models.CharField(
                default="This user has thus far opted to maintain an air of mystery.",
                max_length=1000,
            ),
        ),
    ]
