import json

from django.db import models
from django.utils.translation import gettext as _


def get_default_auto_fields():
    return {"data": []}


class WV(models.Model):
    title = models.CharField(
        _("WebView title"),
        max_length=100,
        blank=False,
        null=False,
        unique=True
    )
    url = models.URLField(max_length=100, blank=False, null=False)
    list_of_auto_fields = models.JSONField(
        default=get_default_auto_fields, max_length=100, blank=False, null=False)

    def __str__(self):
        return self.title
