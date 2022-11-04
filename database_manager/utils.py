import os
import pickle
import uuid

from django.apps import apps

from app.conf import settings


def dump_database(app_name='app'):
    try:
        models = apps.get_app_config(app_name).get_models()
        data = {}
        for model in models:
            data[model.__name__] = model.objects.all()
        if not os.path.exists(os.path.join(settings.BASE_DIR, 'media')):
            os.makedirs(os.path.join(settings.BASE_DIR, 'media'))
        filename = str(uuid.uuid4()) + '.sav'
        filepath = os.path.join(settings.BASE_DIR, 'media', filename)
        with open(filepath, 'wb') as f:
            pickle.dump(data, f)
        f.close()
        return filename
    except Exception as e:
        raise e
