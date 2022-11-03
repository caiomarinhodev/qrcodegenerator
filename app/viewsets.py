import os
import uuid
from urllib.request import pathname2url

import django_filters
import qrcode
from django_filters import rest_framework as filters
from rest_framework import viewsets, views, status
from rest_framework.response import Response

from . import (
    serializers,
    models
)
from .cloudinary_api import upload_file
from .models import Qrcode
from .serializers import QrcodeSerializer


class QrcodeFilter(django_filters.FilterSet):
    class Meta:
        model = models.Qrcode
        fields = ["id", "name", "image_url"]


class QrcodeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.QrcodeSerializer
    queryset = models.Qrcode.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = QrcodeFilter


class GeneratedQrcodeViewSet(views.APIView):
    serializer = QrcodeSerializer

    def generate_qrcode(self, key, name_file):
        qr = qrcode.make(key)
        final_name = '{}.png'.format(name_file)
        final_path = os.path.join('static', 'qrcodes', final_name)
        qr.save(final_path)
        return final_path

    def get_image_url(self, request, path) -> str:
        scheme = request.is_secure() and "https" or "http"
        fixed_path_url = pathname2url(path)
        return f'{scheme}://{request.get_host()}/' + fixed_path_url

    def get(self, request, *args, **kwargs):
        queryset = models.Qrcode.objects.all()
        serializer = self.serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        cleaned_data = request.data
        key = request.data.get("key")
        if 'filename' in cleaned_data:
            filename = cleaned_data.get("filename")
            path = self.generate_qrcode(key, filename)
        else:
            filename = str(uuid.uuid4())
            path = self.generate_qrcode(key, filename)
        try:
            upload_to_server = upload_file(path, filename)
        except(Exception,):
            return Response({"error": "Erro ao enviar imagem para o servidor de imagens"},
                            status=status.HTTP_400_BAD_REQUEST)
        model = self.serializer(data={"key": key, "name": filename, "image_url": upload_to_server['secure_url']})
        if model.is_valid():
            model.save()
            return Response(model.data, status=status.HTTP_201_CREATED)
        return Response(model.errors, status=status.HTTP_400_BAD_REQUEST)


class ValidateQrcodeViewSet(views.APIView):
    serializer = QrcodeSerializer

    def get(self, request, *args, **kwargs):
        queryset = models.Qrcode.objects.all()
        serializer = self.serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.data
        key = data.get("key")
        queryset = Qrcode.objects.filter(key=key)
        if queryset.exists():
            model = self.serializer(queryset.first())
            return Response({"message": "success", "qrcode": model.data}, status=status.HTTP_200_OK)
        return Response({"message": "error"}, status=status.HTTP_400_BAD_REQUEST)
