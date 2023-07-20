from django.db import models
from django.utils.translation import gettext as _


class Subject(models.Model):
    title = models.CharField(
        _("Subject title"),
        max_length=100,
        blank=False,
        null=False
    )
    note = models.CharField(
        _("Additional text"),
        max_length=100,
        blank=False,
        null=False
    )
    direction = models.ManyToManyField("core_api.direction", related_name='direction_subjects', blank=False)


class InfoPost(models.Model):
    title = models.CharField(
        _("Post title"),
        max_length=100,
        blank=False,
        null=False
    )

    subtitle = models.CharField(
        _("Post subtitle"),
        max_length=100,
        blank=False,
        null=False
    )

    source_url = models.URLField(
        _("Post source url"),
        max_length=100,
        blank=True,
        null=False
    )

    content = models.CharField(
        _("Post content"),
        max_length=10000,
        blank=True,
        null=False
    )

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject_info_posts', blank=False, null=False)
