from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _


class PubTag(models.Model):
    title = models.CharField(
        _("Tag title"),
        max_length=100,
        blank=False,
        null=False,
        unique=True
    )


class PubGroup(models.Model):
    title = models.CharField(
        _("Pub Group title"),
        max_length=100,
        blank=False,
        null=False,
        unique=True
    )

    url = models.URLField(
        _("Group url"),
        max_length=100,
        blank=False,
        null=False,
        unique=True
    )

    last_parse = models.DateTimeField(_('Group last parse date'), null=True, blank=False)

    faculties = models.ManyToManyField('core_api.Faculty', related_name='faculty_pub_groups', blank=False)

    tags = models.ManyToManyField(PubTag, related_name='pub_tag_pub_groups', blank=False)


class Publication(models.Model):
    title = models.CharField(
        _("Pub title"),
        max_length=100,
        blank=False,
        null=False,
    )

    body_text = models.TextField(
        _('Pub body text'),
        max_length=10000,
        blank=False
    )

    date = models.DateTimeField(_('Pub time'), default=timezone.now, blank=False, null=False)
    parent_group = models.ForeignKey(PubGroup, on_delete=models.CASCADE, related_name='pub_group_publications', blank=False, null=False)
    tags = models.ManyToManyField(PubTag, related_name='pub_tag_publications', blank=False)


class PubPicture(models.Model):
    order_nb = models.IntegerField(_('Pic order number'), help_text="Starts from 0")
    url = models.URLField(
        _("Pub picture url"),
        max_length=100,
        blank=False,
        null=False
    )
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='publication_pictures', blank=False, null=False)