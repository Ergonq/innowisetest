# Generated by Django 4.0.3 on 2022-05-11 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ticket", "0003_remove_ticketcomment_ticket_ticket_ticket_comment"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ticket",
            name="ticket_comment",
        ),
        migrations.AddField(
            model_name="ticketcomment",
            name="ticket",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="ticket.ticket"
            ),
        ),
    ]
