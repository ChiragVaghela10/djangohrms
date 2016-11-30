from django import forms
from django.forms import ModelForm, CharField, EmailField
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User
from .models import UserProfile

from .validators import validate_username, username_regex, password_regex, email_regex

class SignupForm(ModelForm):
    username = CharField(required=True, validators=[validate_username, username_regex], max_length=150)
    password = CharField(widget=forms.PasswordInput(), required=True, validators=[password_regex], max_length=128)
    first_name = CharField(required=True, error_messages={'required': 'Enter firstname'}, max_length=30)
    email = EmailField(required=True, validators=[email_regex], max_length=254)
    verify_password = CharField(widget=forms.PasswordInput(), required=True, max_length=128)
    
    class Meta:
        model = User  # form will be generated using 'User' table in database

        # following columns of 'User' table will be shown in form and in order
        fields = ['username', 'first_name', 'last_name', 'password', 'email', 'is_active']
        # help_texts = {
        #    'username': _(''),
        # }
        widgets = {
            # 'password' : forms.PasswordInput(),
            'is_active': forms.HiddenInput(),
        }
    def clean(self):
	#rewriting clean method to check whether passwords match or not
	cleaned_data=super(SignupForm,self).clean()
	ps1=cleaned_data.get('password')
	ps2=cleaned_data.get('verify_password')
	if ps1!=ps2:
            msg="Enter same password again"
            self.add_error('verify_password',msg)
	return cleaned_data


class UserAccountForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        help_texts = {
            'username': _(''),
        }


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

        labels = {
            'dob': _('Date of Birth:'),
            'phone_code': _('Country Code:'),
        }



























        ######################### Reference Material ############################################
        # class SigninForm(forms.Form):
        #    username = forms.CharField(label="User name ",required=True)
        #    password = forms.CharField(label="Password ", widget=forms.PasswordInput())


        # email = forms.EmailField(required=True, widget=forms.EmailInput({"placeholder":"Email*"}))
        # retype = forms.CharField(required=True,max_length=128, widget=forms.PasswordInput({"placeholder":"Retype Password*"}))
        # email = forms.CharField(max_length=200, widget=forms.TextInput({ "placeholder": "Text!"}))

        # you can override default widgets
        # widgets = {
        ##    'username' : forms.TextInput({"autofocus":""}),
        ##    'first_name' : forms.TextInput({"required":True,"placeholder":"First Name*","size":"30"}),
        ##    'last_name' : forms.TextInput({"placeholder":"Last Name","size":"30"}),
        #   'password' : forms.PasswordInput(),
        #    'is_active' : forms.HiddenInput(),
        # }

        # You can specify field_classes also
        # field_classes = {
        #    'username': forms.EmailField,
        # } #commented because it has no effect in this example

        # You can specify label for fields
        # labels = {
        #    'username': _('User Name*:'),
        #    'first_name': _('First Name*:'),
        #    'last_name': _('Last Name:'),
        #    'password': _('Password*:'),
        # }

        ##You can create help text for each field too
        # help_texts = {
        #    'username': _(''),
        #    'password' : _('Password must contain Minimum 8 characters, 1 Uppercase, 1 Lowercase and 1 speacial character'),
        # }

        # You can create custom error message
        # error_messages = {
        #    'username': {
        #        'max_length': _("This username is too long."),
        #    },
        #    'first_name': {
        #        'max_length': _("This first name is too long."),
        #    },
        #    'last_name': {
        #        'max_length': _("This last name is too long."),
        #    },
        # }
