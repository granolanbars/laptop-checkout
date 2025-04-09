from django import forms 
from django.core.exceptions import ValidationError
from .models import Laptop, User

class UserForm(forms.Form):
    a_number = forms.CharField(label='A Number', max_length = 9, widget=forms.TextInput(attrs={"id": "user_id"}))
    email = forms.EmailField(label='Email', max_length = 256, widget=forms.TextInput(attrs={"id": "user_email"}))
    first_name = forms.CharField(label='First Name', max_length = 150, widget=forms.TextInput(attrs={"id": "first_name"}))
    last_name = forms.CharField(label='Last Name', max_length = 150, widget=forms.TextInput(attrs={"id": "last_name"}))
    def clean_a_number(self):
        a_number = self.cleaned_data.get('a_number')
        if not a_number.startswith(('A', 'a')) or len(a_number) != 9 or not a_number[1:].isdigit():
            raise ValidationError("A Number must start with 'A' or 'a' followed by 8 digits.")
        if User.objects.filter(a_number__iexact=a_number).exists():
            raise ValidationError("An account with this A Number already exists.")
        return a_number

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not forms.EmailField().clean(email):
            raise ValidationError("Enter a valid email address.")
        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError("An account with this email already exists.")
        return email

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name.isalpha():
            raise ValidationError("First Name must only contain alphabetic characters.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name.isalpha():
            raise ValidationError("Last Name must only contain alphabetic characters.")
        return last_name



class CheckoutForm(forms.Form):
    computer_id = forms.CharField(label='Computer ID', max_length=10, widget=forms.TextInput(attrs={"id": "computer_id"}))
    user_id = forms.CharField(label='A Number', max_length=9, widget = forms.TextInput(attrs= {"id": "user_id"}))

    def clean_computer_id(self):
        computer_id = self.cleaned_data.get('computer_id')
        
        # Check if the Laptop exists
        try:
            laptop = Laptop.objects.get(computer_id__iexact=computer_id)
        except Laptop.DoesNotExist:
            raise ValidationError("Invalid Computer ID.")
        
        # Validate the status
        if laptop.status == 'Checked Out':
            raise ValidationError("This laptop is already checked out.")
        
        return computer_id
    
    def clean_user_id(self):
        user_id = self.cleaned_data.get('user_id')
        if not User.objects.filter(a_number__iexact=user_id).exists():
            raise ValidationError("User ID does not exist.")
        return user_id


class CheckinForm(forms.Form):
    computer_id = forms.CharField(label='Computer ID', max_length = 10, widget = forms.TextInput(attrs={"id": "computer_id"}))

    def clean_user_id(self):
        user_id = self.cleaned_data.get('user_id')
        if not User.objects.filter(a_number__iexact=user_id).exists():
            raise ValidationError("User ID does not exist.")
        return user_id

    def clean_computer_id(self):
        computer_id = self.cleaned_data.get('computer_id')
        
        # Check if the Laptop exists
        try:
            laptop = Laptop.objects.get(computer_id__iexact=computer_id)
        except Laptop.DoesNotExist:
            raise forms.ValidationError("Invalid Computer ID.")
    
        # Validate the status
        if laptop.status == 'Checked In':
            raise forms.ValidationError("This laptop is already checked in.")
        
        return computer_id


    def clean(self):
        cleaned_data = super().clean()
        time_out = cleaned_data.get('time_out')
        time_in = cleaned_data.get('time_in')

        if time_in and time_out and time_in < time_out:
            raise ValidationError("Time In cannot be earlier than Time Out.")
        return cleaned_data
