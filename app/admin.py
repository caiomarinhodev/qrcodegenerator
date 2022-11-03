#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from app.models import *


# Register your models here.


class QrcodeAdmin(admin.ModelAdmin):
    list_filter = []
    search_fields = (
        'id',
    )
    inlines = []
    list_display = ("id", "name", "image_url")


admin.site.register(Qrcode, QrcodeAdmin)
