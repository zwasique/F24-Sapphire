# Generated by Django 5.1.2 on 2024-11-11 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("database", "0004_user_first_name_user_last_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="inbox",
            name="recipient_id",
        ),
        migrations.DeleteModel(
            name="Message",
        ),
        migrations.RemoveField(
            model_name="userpost",
            name="author",
        ),
        migrations.DeleteModel(
            name="UserTag",
        ),
        migrations.RemoveField(
            model_name="usertagmapping",
            name="user",
        ),
        migrations.DeleteModel(
            name="Inbox",
        ),
        migrations.DeleteModel(
            name="UserPost",
        ),
        migrations.DeleteModel(
            name="UserTagMapping",
        ),
    ]
