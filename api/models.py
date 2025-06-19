from django.db import models

# Create your models here.

class TelegramUser(models.Model):
    telegram_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=150, null=True, blank=True)  # ✅ this line
