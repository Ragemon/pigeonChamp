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
    name = models.CharField(blank=True, null=True, max_length=100)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField()
    confirmed = models.BooleanField(default=False)
    mailing_list = models.ForeignKey(to=MailingList, on_delete=models.CASCADE)


    class Meta:
        unique_together = ['email', 'mailing_list',]


class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mailing_list = models.ForeignKey(to=MailingList, on_delete=models.CASCADE)
    subject = models.CharField(max_length=140)
    body = models.TextField()
    started = models.DateTimeField(default=None, null=True)
    finished = models.DateTimeField(default=None, null=True)

    def __str__(self) -> str:
        return str(self.mailing_list) + ">> " + self.subject











