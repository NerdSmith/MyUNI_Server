from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from schedule_api.validators import FileValidator


class Schedule(models.Model):

    def get_schedule_path(self, filename):
        path = f'schedules/' \
               f'{self.course_group.course_number}_' \
               f'{self.course_group.group_number}' \
               f'.{self.course_group.subgroup_number}_' if self.course_group.subgroup_number is not None else '_' \
               f'{self.course_group.education_level}.json'
        return path

    course_group = models.ForeignKey("core_api.CourseGroup",
                                     on_delete=models.CASCADE, related_name='course_group_schedule', blank=False, null=False)
    schedule_file = models.FileField(_('Schedule file'), upload_to=get_schedule_path,
                                     validators=[
                                         FileExtensionValidator(['json']),
                                         FileValidator(limit_value=1024*100)
                                     ],
                                     max_length=50)

    def __str__(self):
        return f"Schedule -> {self.course_group}"
