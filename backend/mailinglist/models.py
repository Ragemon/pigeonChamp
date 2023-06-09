from django.db import models
from django.conf import settings
from django.urls import reverse


import uuid


class MailingList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=140)
    owner = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)



    def __str__(self): return self.name

    def get_absolute_url(self):
        return reverse("mailinglist:manage_mailinglist", kwargs={"pk": self.id})

    def account_can_use_mailing_list(self, account):
        return account == self.owner
    

class Subscriber(models.Model):
    name = models.CharField(blank=True, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField()
    confirmed = models.BooleanField(default=False)
    mailing_list = models.ForeignKey(to=MailingList, on_delete=models.CASCADE)


    class Meta:
        unique_together = ['email', 'mailing_list',]











