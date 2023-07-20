from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext as _

from maps_api.models import Building
from wvs_api.models import WV

User = get_user_model()


class Faculty(models.Model):
    title = models.CharField(
        _("Faculty title"),
        max_length=100,
        blank=False,
        null=False,
        unique=True
    )

    class Meta:
        verbose_name = "Faculty"
        verbose_name_plural = "Faculties"

    def __str__(self):
        return self.title


class Direction(models.Model):
    title = models.CharField(
        _("Direction title"),
        max_length=100,
        blank=False,
        null=False,
        unique=True
    )
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='directions', blank=False, null=False)

    class Meta:
        verbose_name = "Direction"
        verbose_name_plural = "Directions"

    def __str__(self):
        return self.title


class CourseGroup(models.Model):
    course_number = models.IntegerField(_('Course number'), blank=False,
                                        validators=[MinValueValidator(1), MaxValueValidator(5)])

    group_number = models.IntegerField(_('Group number'), blank=False, null=False)
    subgroup_number = models.IntegerField(_('Subgroup number'), blank=True, null=True)

    EDUCATION_LEVELS = [
        ('b', "bachelor"),
        ('m', "magistracy"),
        ('p', "postgraduate"),
        ('s', "specialty")
    ]
    # EDUCATION_LEVELS_RU = {
    #     'b': "бакалавриат",
    #     'm': "магистратура",
    #     'p': "аспирантура",
    #     's': "специалитет"
    # }
    education_level = models.CharField(
        _('Education level'),
        max_length=1, choices=EDUCATION_LEVELS, blank=False, null=False)

    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, related_name='course_groups', blank=False, null=False)

    class Meta:
        verbose_name = "Course Group"
        verbose_name_plural = "Course Groups"

    def __str__(self):
        return f"{self.course_number} course {self.group_number}{f'.{self.subgroup_number}' if self.subgroup_number is not None else ''} group"


class SubList(models.Model):
    title = models.CharField(
        _("Direction title"),
        max_length=100,
        blank=False,
        null=False,
        unique=True
    )
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False, related_name='sub_lists')
    main_direction = models.ForeignKey(Direction, on_delete=models.CASCADE, related_name='direction_sub_lists', blank=False, null=False)

    # smth else

    buildings = models.ManyToManyField(Building, related_name='building_sub_lists', blank=False)

    main_course_group = models.ForeignKey(CourseGroup, on_delete=models.CASCADE, related_name='main_course_group_sub_lists', blank=False, null=False)
    additional_course_groups = models.ManyToManyField(CourseGroup, limit_choices_to=~Q(id=models.F("add_course_group_sub_lists")), related_name='add_course_group_sub_lists', blank=False)

    wvs = models.ManyToManyField(WV, related_name='wv_sub_lists', blank=False)

    def __str__(self):
        return self.title
