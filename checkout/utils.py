from django.core.mail import send_mail
from collections import defaultdict
from .models import Laptop


#email function
def send_reminder_emails():
    # Group laptops by user
    user_laptops = defaultdict(list)
    
    # Fetch laptops still checked out
    overdue_laptops = Laptop.objects.filter(status='Checked Out')
    
    for laptop in overdue_laptops:
        if laptop.checkout_user:
            user_laptops[laptop.checkout_user].append(f"Computer: #{laptop.computer_number} ID: {laptop.computer_id}")

    
    # Send one email per user
    for user, laptop_ids in user_laptops.items():
        laptop_list = ", ".join(laptop_ids)  # Create a comma-separated list of laptop IDs
        email_message = (
            f"Dear {user.first_name},\n\n"
            f"The following laptops are still checked out under your name:\n"
            f"{laptop_list}\n\n"
            "Please return them as soon as possible.\n\n"
            "Thank you!"
        )
        
        send_mail(
            subject="Reminder: Return Your Laptop",
            message=email_message,
            from_email='power@usu.edu',  # Replace with your sender email
            recipient_list=[user.email],  # Replace with the user's email
            fail_silently=False,
        )