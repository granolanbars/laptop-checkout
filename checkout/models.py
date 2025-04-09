import datetime
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

# Create your models here.
class User(models.Model):
    a_number = models.CharField("Anumber", 
        max_length=9, 
        unique = True, 
        validators=[RegexValidator(r'^[Aa]\d{8}$', message="Invalid A number format",),], 
        primary_key = True,
        )
    email = models.EmailField("Email", max_length=321, unique = True)
    first_name = models.CharField("First Name", max_length = 150,)
    last_name = models.CharField("Last Name", max_length = 150,)
    creation_date = models.DateTimeField("Account Creation Date", auto_now_add = True)

    def __str__(self):
        return self.a_number
    

class Laptop(models.Model):

    computer_id = models.CharField("Computer ID", max_length = 10, primary_key=True)
    computer_number = models.CharField("Computer Number", max_length = 10)
    condition = models.CharField("Condition", max_length = 100)
    status = models.CharField(max_length = 20, default = 'Checked In')
    checkout_user = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, null = True, blank = True)

    def __str__(self):
        laptop_number = self.computer_id if self.computer_id else "Unknown Laptop"
        user_anumber = self.checkout_user if self.checkout_user else "Unknown User"
        return f"Laptop: {laptop_number}, User: {user_anumber}"

class Transaction(models.Model):
    transaction_id = models.AutoField("Transaction ID", primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, default=None, blank = True)
    computer_id = models.ForeignKey(Laptop, on_delete=models.SET_NULL, null = True, default=None, blank = True)
    time_out = models.DateTimeField("Time Out", auto_now_add = True)
    time_in = models.DateTimeField("Time In", null = True, blank = True)
    condition_out = models.CharField("Condition Out", max_length = 100,default = None, null = True, blank = True)
    condition_in = models.CharField("Condition In", max_length = 100, default = None, null=True, blank = True)

    def __str__(self):
        return f"#{self.transaction_id} - User: {self.user_id} - Laptop: {self.computer_id}"

    
