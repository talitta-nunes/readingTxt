from unittest.util import _MAX_LENGTH

from django.db import models


# Create your models here.
class ClientForm(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    file = models.FileField(upload_to='files/', null=True, verbose_name="")
