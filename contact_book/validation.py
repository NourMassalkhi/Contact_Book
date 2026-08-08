import re

from .exceptions import ValidationError


def validate_name(name):
    name = name.strip()
    if not name:
        raise ValidationError("Name cannot be empty.")
    if len(name) < 2 or len(name) > 50:
        raise ValidationError("Name must be between 2 and 50 characters.")
    for c in name:
        if not (c.isalpha() or c == " "):
            raise ValidationError("Name can only contain letters and spaces.")

#chevk for phonenumbers library
def validate_phone(phone):
    phone = phone.strip()
    pattern = r"^(?:\+961|961)?(?:0?[13456789]\d{6}|[78]\d{7})$"
    if not re.fullmatch(pattern, phone):
        raise ValidationError("Invalid Lebanese phone number.")

def validate_email(email):
    email = email.strip()
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.fullmatch(pattern, email):
        raise ValidationError("Invalid email address.")