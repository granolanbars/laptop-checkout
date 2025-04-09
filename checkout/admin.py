from django.contrib import admin

# Register your models here.
from .models import User, Laptop, Transaction

class LaptopAdmin(admin.ModelAdmin):
    list_display = ('computer_number', 'status')

admin.site.register(User)
admin.site.register(Laptop)
admin.site.register(Transaction)


