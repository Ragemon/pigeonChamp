from django.contrib import admin
from .models import MailingList, Subscriber, Message
# Register your models here.


class MailingListAdmin(admin.ModelAdmin):
    field = "__all__"

admin.site.register(MailingList, MailingListAdmin)

class SubscriberAdmin(admin.ModelAdmin):
    field = "__all__"

admin.site.register(Subscriber, SubscriberAdmin)

class MessageAdmin(admin.ModelAdmin):
    field = "__all__"



admin.site.register(Message, MessageAdmin)
