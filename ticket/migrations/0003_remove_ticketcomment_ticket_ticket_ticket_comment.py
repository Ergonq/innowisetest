# Generated by Django 4.0.3 on 2022-05-11 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ticket", "0002_alter_ticket_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ticketcomment",
            name="ticket",
        ),
        migrations.AddField(
            model_name="ticket",
            name="ticket_comment",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="ticket.ticketcomment"
            ),
        ),
    ]
