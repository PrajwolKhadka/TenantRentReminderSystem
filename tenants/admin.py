# from datetime import timezone
# from django.contrib import admin
# # from nepali_datetime import timezone

# from .models import Tenant, ReminderLog

# @admin.register(Tenant)
# class TenantAdmin(admin.ModelAdmin):
#     list_display = ('name', 'phone_number', 'rent_amount', 'due_day', 'last_payment_date')
#     list_filter = ('due_day',)
#     search_fields = ('name', 'phone_number')
#     # Add the custom action here
#     actions = ['mark_as_paid']

#     def mark_as_paid(self, request, queryset):
#         today= timezone.now().date()
#         updated_count = queryset.update(last_payment_date=today)
        
#         # for tenant in queryset:
#         #     last_log = ReminderLog.objects.filter(tenant=tenant).order_by('-sent_at').first()
#         #     if last_log:
#         #         last_log.paid = True
#         #         last_log.save()

#         for tenant in queryset:
#                 last_log = ReminderLog.objects.filter(tenant=tenant).order_by('-sent_at').first()
#                 if last_log:
#                     last_log.paid = True
#                     last_log.save()
#         self.message_user(request, f"{updated_count} tenant(s) successfully marked as paid as of today.")

# @admin.register(ReminderLog)
# class ReminderLogAdmin(admin.ModelAdmin):
#     list_display = ('tenant', 'sent_at', 'method', 'status', 'paid')


# from datetime import timezone
from django.utils import timezone
from django.contrib import admin
from django.utils.html import format_html
from django.urls import path
from django.shortcuts import redirect

from .models import Tenant, ReminderLog

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'rent_amount', 'due_day', 'last_payment_date', 'mark_as_paid_button')
    list_filter = ('due_day',)
    search_fields = ('name', 'phone_number')
    actions = ['mark_as_paid']

    def mark_as_paid(self, request, queryset):
        today = timezone.now().date()
        updated_count = queryset.update(last_payment_date=today)
        
        for tenant in queryset:
            last_log = ReminderLog.objects.filter(tenant=tenant).order_by('-sent_at').first()
            if last_log:
                last_log.paid = True
                last_log.save()

        self.message_user(request, f"{updated_count} tenant(s) successfully marked as paid as of today.")

    def mark_as_paid_button(self, obj):
        return format_html(
            '<a class="btn btn-success" href="{}">Mark as Paid</a>',
            f'{obj.id}/mark-paid/'
        )
    mark_as_paid_button.short_description = 'Action'
    mark_as_paid_button.allow_tags = True 

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:tenant_id>/mark-paid/', self.admin_site.admin_view(self.mark_paid_view), name='tenant-mark-paid'),
        ]
        return custom_urls + urls

    def mark_paid_view(self, request, tenant_id):
        tenant = Tenant.objects.get(id=tenant_id)
        tenant.last_payment_date = timezone.now().date()
        tenant.save()

        last_log = ReminderLog.objects.filter(tenant=tenant).order_by('-sent_at').first()
        if last_log:
            last_log.paid = True
            last_log.save()

        self.message_user(request, f"{tenant.name} marked as paid today.")
        return redirect(request.META.get('HTTP_REFERER'))

@admin.register(ReminderLog)
class ReminderLogAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'sent_at', 'method', 'status', 'paid')
