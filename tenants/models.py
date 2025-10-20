from django.db import models

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_day = models.IntegerField(help_text="Day of the month rent is due (1-31)")
    last_payment_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.phone_number}"


class ReminderLog(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=20, choices=[('WhatsApp', 'WhatsApp')])
    status = models.CharField(max_length=20, choices=[('Sent', 'Sent'), ('Failed', 'Failed')])
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Reminder to {self.tenant.name} on {self.sent_at.date()}"

