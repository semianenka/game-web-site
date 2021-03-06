from django import forms
from django.utils import timezone
from django.contrib.auth.hashers import check_password

BIRTH_YEAR_CHOICES = [i for i in range(timezone.now().year - 100, timezone.now().year + 1)]


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=16,
        required=True,
        widget=forms.TextInput({'placeholder': 'Enter username here...', 'class': 'form-input'})
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput({'placeholder': 'Enter password here...', 'class': 'form-input'})
    )


class SignUpForm(forms.Form):
    username = forms.CharField(
        max_length=16,
        required=True,
        widget=forms.TextInput({'placeholder': 'Enter username here...', 'class': 'form-input'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput({'placeholder': 'Enter email here...', 'class': 'form-input'})
    )
    first_name = forms.CharField(
        max_length=64,
        required=True,
        widget=forms.TextInput({'placeholder': 'Enter first name here...', 'class': 'form-input'})
    )
    last_name = forms.CharField(
        max_length=64,
        required=True,
        widget=forms.TextInput({'placeholder': 'Enter last name here...', 'class': 'form-input'})
    )
    birth_date = forms.DateField(
        required=True,
        widget=forms.SelectDateWidget({'class': 'form-input'}, years=BIRTH_YEAR_CHOICES)
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput({'placeholder': 'Enter password here...', 'class': 'form-input'})
    )
    confirm_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput({'placeholder': 'Confirm password...', 'class': 'form-input'})
    )

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        if str(cleaned_data['password']) != str(cleaned_data['confirm_password']):
            raise forms.ValidationError('Passwords don\'t match')
        return cleaned_data
