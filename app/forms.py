from django import forms
from django.forms import ModelForm

from app.utils import generate_bootstrap_widgets_for_all_fields
from . import (
    models
)


class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # field.widget.attrs['class'] = 'form-control'
            if field_name == 'phone' or field_name == 'telefone':
                field.widget.attrs['class'] = 'form-control telefone phone'
            if field_name == 'cep' or field_name == 'postalcode':
                field.widget.attrs['class'] = 'form-control cep'


class QrcodeForm(BaseForm, ModelForm):
    class Meta:
        model = models.Qrcode
        fields = ("id", "name", "key", "image_url", "qrcode")
        widgets = generate_bootstrap_widgets_for_all_fields(models.Qrcode)

    def __init__(self, *args, **kwargs):
        super(QrcodeForm, self).__init__(*args, **kwargs)


class QrcodeFormToInline(BaseForm, ModelForm):
    class Meta:
        model = models.Qrcode
        fields = ("id", "name", "image_url")
        widgets = generate_bootstrap_widgets_for_all_fields(models.Qrcode)

    def __init__(self, *args, **kwargs):
        super(QrcodeFormToInline, self).__init__(*args, **kwargs)
