from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, \
    AuthenticationForm, PasswordChangeForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from crispy_forms.bootstrap import FormActions
from .models import Account


class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_registrationForm'
        self.helper.form_class = 'blueForms'
        self.helper.layout = Layout(
            'username',
            'password1',
            'password2',
            FormActions(Submit('register', 'Register',
                               css_class='btn-primary.btn-block'))
        )
        super(RegistrationForm, self).__init__(*args, **kwargs)


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_loginForm'
        self.helper.form_class = 'blueForms'
        self.helper.layout = Layout(
            'username',
            'password',
            FormActions(Submit('login', 'Login',
                               css_class='btn-primary.btn-block'))
        )
        super(LoginForm, self).__init__(*args, **kwargs)


class PasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(PasswordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_passwordForm'
        self.helper.form_class = 'blueForms'
        self.helper.layout = Layout(
            'old_password',
            'new_password1',
            'new_password2',
            FormActions(Submit('update', 'Update',
                               css_class='btn-primary.btn-block'))
        )
        super(PasswordForm, self).__init__(*args, **kwargs)


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_profileForm'
        self.helper.form_class = 'blueForms'
        self.helper.layout = Layout(
            'picture',
            'home',
            'interests',
            'objectives',
            FormActions(Submit('update', 'Update',
                               css_class='btn-primary.btn-block')))

    class Meta:
        model = Account
        fields = ['picture', 'home', 'interests', 'objectives']


class UserDataForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserDataForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_userdataForm'
        self.helper.form_class = 'blueForms'
        self.helper.layout = Layout(
            'username',
            Field('password', type='hidden'),
            # Field('date_joined', type='hidden'),
            # Field('last_login', type='hidden'),
            # 'first_name',
            # 'last_name',
            # 'email',
            FormActions(Submit('update', 'Update',
                               css_class='btn-primary.btn-block')))

    class Meta:
        model = User
        fields = ['username', 'password']
        # fields = ['username', 'password', 'first_name', 'last_name',
        #           'email', 'date_joined', 'last_login']
