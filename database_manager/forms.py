import pickle

from django import forms
from django.apps import apps

CHOICES = [str(i.label) for i in apps.get_app_configs() if i.label != 'django' and (i != '' or i is not None)]


class FileUploadForm(forms.Form):
    file = forms.FileField()
    with_delete = forms.BooleanField(required=False)
    app = forms.ChoiceField(choices=[(i, i) for i in CHOICES])

    def __init__(self, *args, **kwargs):
        super(FileUploadForm, self).__init__(*args, **kwargs)
        self.fields['with_delete'].label = 'Delete all database before loading new data'

    def clean(self):
        cleaned_data = super(FileUploadForm, self).clean()
        file = cleaned_data.get('file')
        if file:
            if file.name.split('.')[-1] != 'sav':
                raise forms.ValidationError('File must be a SAV file')
        return cleaned_data

    def save(self, *args, **kwargs):
        file = self.cleaned_data.get('file')
        with_delete = self.cleaned_data.get('with_delete')
        app = self.cleaned_data.get('app')
        if with_delete:
            models = apps.get_app_config(app).get_models()
            for model in models:
                model.objects.all().delete()
        if file:
            data = pickle.load(file)
            for model_name, model_data in data.items():
                for item in model_data:
                    item.save()
            return True
        return False
