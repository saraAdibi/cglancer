from django.contrib import admin
from .models import ContactMessage
from .forms import ContactMessageForm


class ContactMessageAdmin(admin.ModelAdmin):
    form = ContactMessageForm


admin.site.register(ContactMessage, ContactMessageAdmin)
