from rest_framework import serializers

from app.models import Qrcode


class QrcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qrcode
        fields = ("id", "name", "key", "image_url")
