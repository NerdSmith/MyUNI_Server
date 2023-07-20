import json

import jsonschema
from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible
from rest_framework.exceptions import ValidationError

from .schedule_schemas.schedule_schema_v_1 import schedule as schedule_scheme_v_1


@deconstructible
class FileValidator(BaseValidator):
    def __call__(self, data):
        try:
            jsonschema.validate(json.load(data), schedule_scheme_v_1)
        except Exception as e:
            raise ValidationError("Schedule file is corrupted!")
