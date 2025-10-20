from apscheduler.schedulers.background import BackgroundScheduler
from django.utils import timezone
from .models import Tenant, ReminderLog
from .notifications import send_whatsapp_message
from decouple import config
PHONE_NUMBER = config("PHONE_NUMBER")
scheduler = BackgroundScheduler()
scheduler.start()

def send_due_reminders():
    today = timezone.localdate()

    due_tenants = Tenant.objects.filter(due_day=today.day)

    for tenant in due_tenants:
        # Skip if already paid this month
        if tenant.last_payment_date and tenant.last_payment_date.year == today.year and tenant.last_payment_date.month == today.month:
            continue
        
        message = f"""
        Hello {tenant.name}, your rent of Rs.{tenant.rent_amount} is due today.
        You can use services like eSewa/Khalti or Cash to complete the transaction.
        You can pay the rent on the id (9841394638) on eSewa or Khalti.

        नमस्ते {tenant.name}, तपाईंको {tenant.rent_amount} रुपैयाँ भाडा बाँकी छ।
        कारोबार पूरा गर्न तपाईंले eSewa/Khalti वा Cash जस्ता सेवाहरू प्रयोग गर्न सक्नुहुन्छ।
        तपाईंले eSewa वा Khalti मा id ({PHONE_NUMBER}) मार्फत भाडा तिर्न सक्नुहुन्छ।

        ***This message will be sent every 8 hours until the dues are cleared***
        ***यो सन्देश बक्यौता चुक्ता नभएसम्म हरेक ८ घण्टामा पठाइनेछ।***
        """
        try:
            # send_whatsapp_message(tenant.phone_number, message)
            # ReminderLog.objects.create(tenant=tenant, method='WhatsApp', status='Sent', paid=False)
            print(f"Sending WhatsApp message to {tenant.phone_number}")
            print("Message content:", message)
            send_whatsapp_message(tenant.phone_number, message)
            ReminderLog.objects.create(tenant=tenant, method='WhatsApp', status='Sent', paid=False)
        except Exception as e:
            print(f"Failed to send message: {e}")
            ReminderLog.objects.create(tenant=tenant, method='WhatsApp', status='Failed', paid=False)


# def send_due_reminders():
#     print("Scheduler triggered")
#     today = timezone.localdate()
#     due_tenants = Tenant.objects.all()  # ignore due_day for testing

#     for tenant in due_tenants:
#         message = f"Hello {tenant.name}, this is a test WhatsApp message from Django"
#         try:
#             send_whatsapp_message(tenant.phone_number, message)
#             print(f"Message sent to {tenant.phone_number}")
#             ReminderLog.objects.create(tenant=tenant, method='WhatsApp', status='Sent', paid=False)
#         except Exception as e:
#             print(f"Failed to send message: {e}")

# Fort test only!!!!!!!!!!!
# scheduler.add_job(send_due_reminders, 'interval', seconds=2)

#Production ko lagi, 6 hours interval ma msg pathauxa!!!!!!!!!!!
scheduler.add_job(send_due_reminders, 'cron', hour='8,14,20', minute=30)
