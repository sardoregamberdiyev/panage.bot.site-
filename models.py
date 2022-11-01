from django.db import models


# Create your models here.


class Log(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    message = models.JSONField(default={"state": 0})


class TgUser(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=256, null=True, blank=True)
    last_name = models.CharField(max_length=256, null=True, blank=True)
    user_name = models.CharField(max_length=256, null=True, blank=True)
    phone = models.CharField(max_length=56, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name}"
