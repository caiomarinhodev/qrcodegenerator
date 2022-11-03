# Create your models here.
import os

from django.db import models


class Timestamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Qrcode(Timestamp):
    name = models.CharField(max_length=255, blank=True, null=True)
    key = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    qrcode = models.ImageField(upload_to=os.path.join('static', 'qrcodes'), blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'QR Code'
        verbose_name_plural = 'QR Codes'
