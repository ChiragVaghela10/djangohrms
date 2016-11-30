from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from datetime import date
from django.core.validators import RegexValidator


# from django.core.exceptions import ValidationError
# Custom Validator:
# def street_validator(value):
#    if re.search(r'^([a-zA-Z]+)$',value):
#        raise ValidationError(
#            _("Street1 shouldn't contain alphabets only, enter street number too."),
#        )   

class UserProfile(models.Model):
    COUNTRY_CODES = (
        ('+91', 'India(+91)'),
        ('+1', 'USA(+1)'),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    dob = models.DateField(default=date.today)
    phone_code = models.CharField(
        max_length=3,
        choices=COUNTRY_CODES,
        blank=True
    )
    # we're using in-built Regex Validator
    phone_regex = RegexValidator(regex=r'^\d{10}$', message="Phone number must be 10 digits number.")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, default=0)  # validators should be a list
    street1 = models.CharField(max_length=5, blank=True, default='')  # validators=[street_validator],
    street2 = models.CharField(max_length=50, blank=True, default='')
    city = models.CharField(max_length=50, blank=True, default='')
    state = models.CharField(max_length=50, blank=True, default='')
    pincode_regex = RegexValidator(regex=r'^\d{6}$', message="PINCODE must be 6 digits number.")
    pincode = models.CharField(validators=[pincode_regex], blank=True, max_length=6, default='')

    def __str__(self):
        """
        It decides what to display when access objects from console
        """
        return "%s" % self.user.username

        # class JobProfile(models.Model):
        #    JOB_CODES = (
        #        ('SD','SOFTWARE DEVELOPER'),
        #        ('AE','APPLICATION ENGINEER'),
        #        ('WD','WEB DEVELOPER'),
        #    )
        #    DEP_CODES = (
        #        ('RND','Research & Development'),
        #        ('MKT','Marketing'),
        #        ('SALS','Sales'),
        #    )
        #    user = models.OneToOneField(
        #        User,
        #        on_delete=models.CASCADE,
        #        primary_key=True,
        #    )
        #    job_title = models.CharField(
        #        max_length=4,
        #        choices=JOB_CODES,
        #        blank=True
        #    )
        #    secondary_job_title = models.CharField(max_length=15,blank=True,default='')
        #    reportsto = models.CharField(max_length=15,blank=True,default='')    #need to be improved
        #    department = models.CharField(
        #        max_length=4,
        #        choices=DEP_CODES,
        #        blank=True
        #    )
