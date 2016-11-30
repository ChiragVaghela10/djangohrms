from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator 

username_regex = RegexValidator(regex=r'^[A-Za-z0-9_]+$', message="Enter alphanumeric and underscore only")
password_regex = RegexValidator(regex=r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{5,12}$', message="Must contain one capital letter, one small letter, one digit and length between 5-12 characters")    
email_regex = RegexValidator(regex=r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z0-9]{2,4}$', message="Please Enter Valid Email")    

def validate_username(value):
    if value == '' or len(value)<3:
        raise ValidationError(
        _('Username cannot be empty or requires 3 characters atleast'),
        code='invalid'
        )