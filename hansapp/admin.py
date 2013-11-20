from django.contrib import admin

from hansapp import models


for item in [getattr(models, attr) for attr in dir(models)]:
    if 'django.db.models.base.ModelBase' in str(item.__class__):
        admin.site.register(item)

