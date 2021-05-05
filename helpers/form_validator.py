
from django.core.exceptions import ValidationError


def validate_year_class(value):

    if len(str(value)) == 4:
        return value
    else:
        raise ValidationError("Le format n'est pas bon")
