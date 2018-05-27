from django.core.exceptions import ValidationError

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            ('%(value)s is not an even number'),
            params={'value': value},
        )

def clean_email(value):
        email = value
        if ".edu" in email:
            raise ValidationError("We do not accept edu email")

CATEGORIES = ['Mexicon','Asian','Americon','Whatever']

def validation_category(value):
    cat = value.capitalize()
    if not value in CATEGORIES and not cat in CATEGORIES:
        raise ValidationError(f"{value} not a valid category")

LOCATIONS = ['Bangalore','Delhi','Pune','Hyderabad']

def validation_location(value):
    loc = value.capitalize()
    if not value in LOCATIONS and not loc in LOCATIONS:
        raise ValidationError(f"{value} not in valid locations")