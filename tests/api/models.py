from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from tests.models import TestModel


class UploadFileModel(models.Model):
    codes = (
        ('cp1250', 'Testownikowy'),
        ('utf-8', 'UTF-8')
        #  ('', 'Inny'),
    )
    test_choice = models.ForeignKey(TestModel)
    encoding = models.CharField(choices=codes)