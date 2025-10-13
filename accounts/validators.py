from django.core.exceptions import ValidationError
import os

def allow_only_images_validator(val):
    valid_extensions = ['.jpg', '.jpeg', '.png']
    ext = os.path.splitext(val.name)[1]
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension. Allowed extensions are: ' + ', '.join(valid_extensions))