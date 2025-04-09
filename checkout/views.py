# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.views.decorators.cache import never_cache
# from django.contrib import messages
# from django.utils import timezone



# from .models import User, Laptop, Transaction
# from .forms import *


# def actions(request):
#     return render(request, 'checkout/home.html')

# def checkin(request):

#     if request.method == 'POST':
#         form = CheckinForm(request.POST)
#         if form.is_valid():
#             computer_id = form.cleaned_data['computer_id']

#             try:
#                 #Update laptop table
#                 laptop = Laptop.objects.get(computer_id=computer_id)

#                 #check if checked out
#                 if laptop.status == 'checked_out':
#                     form.add_error('computer_id', 'This laptop is already checked in.')

#                 else:
#                     laptop.status = 'checked_in'
#                     laptop.checkout_user = None
#                     laptop.save()
                    
#                     #update transaction
#                     transaction = Transaction.objects.filter(computer_id = laptop, time_in__isnull=True).first()
#                     if transaction:
#                         transaction.time_in = timezone.now()
#                         transaction.condition_in = laptop.condition
#                         transaction.save()

                    
#                     messages.success(request, 'Check-in successful!')
#                     return redirect('actions')
#             except Laptop.DoesNotExist:
#                 form.add_error('computer_id', 'Invalid Computer ID')

#     else:
#         form = CheckinForm()

#     return render(request, 'checkout/check_in.html', {'form': form})

# def checkout(request):
#     if request.method == 'POST':
#         form = CheckoutForm(request.POST)
#         if form.is_valid():
#             computer_id = form.cleaned_data['computer_id']
#             user_id = form.cleaned_data['user_id']

#             # Initialize error tracking
#             errors_found = False

#             try:
#                 # Attempt to fetch the Laptop object
#                 laptop = Laptop.objects.get(computer_id=computer_id)

#                 # Check laptop status
#                 if laptop.status != 'checked_in':
#                     form.add_error('computer_id', 'This laptop is already checked out.')
#                     errors_found = True
#             except Laptop.DoesNotExist:
#                 form.add_error('computer_id', 'Invalid Computer ID')
#                 errors_found = True
#                 print("Laptop does not exist.")

#             try:
#                 # Attempt to fetch the User object
#                 user = User.objects.get(a_number=user_id)
#             except User.DoesNotExist:
#                 form.add_error('user_id', 'Invalid User ID')
#                 errors_found = True
#                 print("User does not exist.")

#             # If there are no errors, proceed with successful checkout
#             if not errors_found:
#                 # Update laptop status
#                 laptop.status = 'Checked Out'
#                 laptop.checkout_user = user
#                 laptop.save()

#                 # Update Transactions Table
#                 transaction = Transaction(
#                     user_id=user,
#                     computer_id=laptop,
#                     time_out=timezone.now(),
#                     condition_out=laptop.condition
#                 )
#                 transaction.save()

#                 # Success message and redirect
#                 messages.success(request, 'Checkout successful!')
#                 return redirect('actions')

#         # Form is invalid or errors occurred
#         return render(request, "checkout/checkout.html", {'form': form})

#     else:
#         form = CheckoutForm()

#     return render(request, "checkout/checkout.html", {'form': form})
# @never_cache
# def create_account(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             # Create a new User object manually
#             try:
#                 User.objects.create(
#                     a_number=form.cleaned_data['a_number'],
#                     email=form.cleaned_data['email'],
#                     first_name=form.cleaned_data['first_name'],
#                     last_name=form.cleaned_data['last_name']
#                 )
#                 # Success message
#                 messages.success(request, 'Account created successfully!')
#                 return redirect('actions')
#             except Exception as e:
#                 # Handle potential errors (e.g., duplicate a_number or email)
#                 messages.error(request, f"Error creating account: {str(e)}")

#     else:
#         form = UserForm()

#     return render(request, "checkout/create_account.html", {'form': form})

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.contrib.messages import get_messages
from django.utils import timezone
from .models import User, Laptop, Transaction
from .forms import *

def actions(request):
    return render(request, 'checkout/home.html')

def checkin(request):
    if request.method == 'POST':
        form = CheckinForm(request.POST)
        if form.is_valid():
            computer_id = form.cleaned_data['computer_id']

            # Get the laptop and update its status
            laptop = Laptop.objects.get(computer_id=computer_id)
            laptop.status = 'Checked In'
            laptop.checkout_user = None
            laptop.save()
            
            # Update the associated transaction
            transaction = Transaction.objects.filter(computer_id=laptop, time_in__isnull=True).first()
            if transaction:
                transaction.time_in = timezone.now()
                transaction.condition_in = laptop.condition
                transaction.save()

            # Success message
            messages.success(request, 'Check-in successful!')
            response = render(request, 'checkout/check_in.html', {'form': form, 'redirect_url': '/'})

            storage = get_messages(request)
            for _ in storage:
                pass  # Iterate through messages to clear them
            return response

    else:
        form = CheckinForm()

    return render(request, 'checkout/check_in.html', {'form': form})

def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            computer_id = form.cleaned_data['computer_id']
            user_id = form.cleaned_data['user_id']

            # Fetch the laptop and update its status
            laptop = Laptop.objects.get(computer_id=computer_id)
            user = User.objects.get(a_number=user_id)

            laptop.status = 'Checked Out'
            laptop.checkout_user = user
            laptop.save()

            # Create a new transaction
            transaction = Transaction(
                user_id=user,
                computer_id=laptop,
                time_out=timezone.now(),
                condition_out=laptop.condition
            )
            transaction.save()

            # Success message
            messages.success(request, 'Checkout successful!')

            response = render(request, 'checkout/checkout.html', {'form': form, 'redirect_url': '/'})

            storage = get_messages(request)
            for _ in storage:
                pass  # Iterate through messages to clear them
            return response

    else:
        form = CheckoutForm()

    return render(request, "checkout/checkout.html", {'form': form})

@never_cache
def create_account(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Create a new User object
            User.objects.create(
                a_number=form.cleaned_data['a_number'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            # Success message
            messages.success(request, 'Account created successfully!')
            response = render(request, 'checkout/create_account.html', {'form': form, 'redirect_url': '/'})

            storage = get_messages(request)
            for _ in storage:
                pass  # Iterate through messages to clear them
            return response
    else:
        form = UserForm()

    return render(request, "checkout/create_account.html", {'form': form})


