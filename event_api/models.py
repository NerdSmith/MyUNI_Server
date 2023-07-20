from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _


class Event(models.Model):
    title = models.CharField(
        _('Event title'),
        max_length=100,
        blank=False,
        null=False
    )
    description = models.TextField(
        _('Event description'),
        max_length=800,
        blank=False,
        null=False
    )

    event_start_datetime = models.DateTimeField(_('Event start date'), default=timezone.now)
    event_end_datetime = models.DateTimeField(_('Event end date'), default=timezone.now)
    is_full_day = models.BooleanField(
        _('Is event full day'),
        default=True,
    )
    course_groups = models.ManyToManyField(
        "core_api.CourseGroup",
        blank=True,
        default=None,
        symmetrical=False,
        related_name="course_group_events"
    )

    EVENT_TYPES = [
        ('i', "Info"),
        ('e', "Exam"),
        ('a', "Attestation"),
        ('h', "Holiday"),
    ]

    e_type = models.CharField(_("Event type"), max_length=1, choices=EVENT_TYPES, blank=False, null=False)

    def __str__(self):
        return self.title
