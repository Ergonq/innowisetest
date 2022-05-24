from django.db import models

# Create your models here.


class Ticket(models.Model):

    """Ticket model"""

    SOLVED, UNSOLVED, FREEZE = range(3)

    status_choices = (
        (SOLVED, "Solved"),
        (UNSOLVED, "Unsolved"),
        (FREEZE, "Freeze"),
    )

    title = models.CharField("Title", max_length=100, blank=True, null=True)
    message = models.TextField("Message", max_length=1000, blank=True, null=True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, blank=True, null=True)
    admin_response = models.TextField("Admin Response", max_length=1000, blank=True, null=True)
    status = models.PositiveSmallIntegerField("Status", choices=status_choices, default=UNSOLVED)

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"
        ordering = ["-id"]

    def __str__(self):
        return self.title


class TicketComment(models.Model):

    """Ticket comment model"""

    message = models.TextField("Ticket Message", max_length=1000, blank=True, null=True)
    admin_response = models.TextField("Admin Response", max_length=1000, blank=True, null=True)
    ticket = models.ForeignKey("ticket.Ticket", on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Ticket Comment"
        verbose_name_plural = "Ticket Comments"
        ordering = ["-id"]

    def __str__(self):
        return f"{self.ticket}"
