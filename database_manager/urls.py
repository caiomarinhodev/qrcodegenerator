from django.urls import path

from database_manager.views import IndexView, DumpDatabaseRedirectView, LoadDatabaseView

urlpatterns = []

urlpatterns += [
    path('', IndexView.as_view(), name='database'),
    path('dump/', DumpDatabaseRedirectView.as_view(), name='dump'),
    path('load/', LoadDatabaseView.as_view(), name='load'),
]
