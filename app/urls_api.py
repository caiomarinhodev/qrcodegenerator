from django.urls import path
from rest_framework.routers import DefaultRouter

from app import (
    viewsets
)

api_urlpatterns = [
    path('api/generate/', viewsets.GeneratedQrcodeViewSet.as_view(), name='generate'),
    path('api/validate/', viewsets.ValidateQrcodeViewSet.as_view(), name='validate'),
]

qrcode_router = DefaultRouter()

qrcode_router.register(
    r'^api/qrcode',
    viewsets.QrcodeViewSet,
    basename="qrcode",
)

api_urlpatterns += qrcode_router.urls
