#! /usr/bin/python
# -*- coding: UTF-8 -*-
"""
Global variables for base module
"""
from django.conf import LazySettings
from django.utils.translation import ugettext_lazy as _

settings = LazySettings()


def get_from_settings_or_default(var_name, default):
    try:
        return settings.__getattr__(var_name)
    except AttributeError:
        return default


# Items by page on paginator views
ITEMS_BY_PAGE = 10

CREATE_SUFFIX = "_create"
LIST_SUFFIX = "_list"
DETAIL_SUFFIX = "_detail"
UPDATE_SUFFIX = "_update"
DELETE_SUFFIX = "_delete"

API_SUFFIX = "_api"
style = "base_django/flexbox"

# Messages
OBJECT_CREATED_SUCCESSFULLY = _("Object created successfully")
OBJECT_UPDATED_SUCCESSFULLY = _("Object updated successfully")
OBJECT_DELETED_SUCCESSFULLY = _("Object deleted successfully")

BASE_MODELS_TRANSLATION_NAME = _("Name")
BASE_MODELS_TRANSLATION_DESCRIPTION = _("Description")
BASE_MODELS_TRANSLATION_SLUG = _("Slug")
BASE_MODELS_TRANSLATION_CREATED = _("Created")
BASE_MODELS_TRANSLATION_MODIFIED = _("Modified")
BASE_MODELS_TRANSLATION_ACTIVE = _("Active")

CONFIGURING_APPLICATION = _("Configuring application {}")
CREATING_PERMISSION_WITH_NAME = _("Creating Permission with name {}")
CREATING_GROUP_WITH_NAME = _("Creating Group with name {}")

QRCODE_PREFIX = "QRCODE"

QRCODE_VERBOSE_NAME = _("Qrcode")
QRCODE_VERBOSE_NAME_PLURAL = _("Qrcode")

QRCODE_LIST_URL_NAME = QRCODE_PREFIX + LIST_SUFFIX
QRCODE_CREATE_URL_NAME = QRCODE_PREFIX + CREATE_SUFFIX
QRCODE_DETAIL_URL_NAME = QRCODE_PREFIX + DETAIL_SUFFIX
QRCODE_UPDATE_URL_NAME = QRCODE_PREFIX + UPDATE_SUFFIX
QRCODE_DELETE_URL_NAME = QRCODE_PREFIX + DELETE_SUFFIX
QRCODE_LIST_JSON_URL_NAME = QRCODE_PREFIX + '_list_json'
