from django.core.exceptions import ValidationError
import re


def validate_email(value):
    """Validate email"""

    pattern = r"[\w-]{1,20}@gmail\.com"
    if not re.match(pattern, value):
        raise ValidationError("Enter a valid email address.", params={"value": value})

