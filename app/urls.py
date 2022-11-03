from django.urls import path, include

from app import conf
from app.urls_api import api_urlpatterns

urlpatterns = []

urlpatterns += [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls'))
]

from app.views import qrcode

urlpatterns += [
    path(
        '',
        qrcode.QrcodeScanView.as_view(),
        name='index'
    ),
    # qrcode
    path(
        'qrcode/',
        qrcode.List.as_view(),
        name=conf.QRCODE_LIST_URL_NAME
    ),
    path(
        'qrcode/full/',
        qrcode.ListFull.as_view(),
        name='QRCODE_list_full'
    ),
    path(
        'qrcode/create/',
        qrcode.Create.as_view(),
        name=conf.QRCODE_CREATE_URL_NAME
    ),
    path(
        'qrcode/<int:pk>/',
        qrcode.Detail.as_view(),
        name=conf.QRCODE_DETAIL_URL_NAME
    ),
    path(
        'qrcode/<int:pk>/update/',
        qrcode.Update.as_view(),
        name=conf.QRCODE_UPDATE_URL_NAME
    ),
    path(
        'qrcode/<int:pk>/delete/',
        qrcode.Delete.as_view(),
        name=conf.QRCODE_DELETE_URL_NAME
    ),
    path(
        'qrcode/list/json/',
        qrcode.QrcodeListJson.as_view(),
        name=conf.QRCODE_LIST_JSON_URL_NAME
    )
]

urlpatterns += api_urlpatterns
