from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler
from django.utils import timezone
import os

class TenantsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tenants'

    def ready(self):
            if os.environ.get('RUN_MAIN', None) != 'true':
                return 
            from .scheduler import send_due_reminders
            scheduler = BackgroundScheduler()
            scheduler.add_job(send_due_reminders, 'cron', hour='8,14,20', minute=30)
            # scheduler.add_job(send_due_reminders, 'interval', seconds=40)
            scheduler.start()
            print("Scheduler started once!")