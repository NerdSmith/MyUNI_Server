import os

from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models
from pytils.translit import slugify
from django.utils.translation import gettext as _


User = get_user_model()


def transliterate_filename(filename):
    name, ext = os.path.splitext(filename)
    name = slugify(name)
    return f'{name}{ext}'


class Building(models.Model):
    title = models.CharField(
        _("Building title"),
        max_length=100,
        blank=False,
        null=False,
        unique=True
    )

    faculties = models.ManyToManyField('core_api.Faculty', related_name='faculty_buildings', blank=False)

    class Meta:
        verbose_name = "Building"
        verbose_name_plural = "Buildings"

    def __str__(self):
        return self.title


class Map(models.Model):

    def get_map_path(self, filename):
        path = f'maps/{transliterate_filename(str(self.building))}_{self.level}.png'
        return path

    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='building_maps', blank=False,
                                 null=False)
    level = models.IntegerField(_('Floor'))
    map_file = models.FileField(upload_to=get_map_path,
                                validators=[
                                    FileExtensionValidator(['png'])
                                ], blank=False, null=False)

    class Meta:
        verbose_name = "Map"
        verbose_name_plural = "Maps"

    def __str__(self):
        return f'{self.building} {self.level} floor'
