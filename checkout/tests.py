from django.test import TestCase
from .models import User, Laptop, Transaction

class UserModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            a_number="A12345678",
            email="testuser@example.com",
            first_name="Test",
            last_name="User"
        )

    def test_user_creation(self):
        self.assertEqual(self.user.a_number, "A12345678")
        self.assertEqual(self.user.email, "testuser@example.com")
        self.assertEqual(self.user.first_name, "Test")
        self.assertEqual(self.user.last_name, "User")

    def test_user_string_representation(self):
        self.assertEqual(str(self.user), "A12345678")


class LaptopModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            a_number="A12345678",
            email="testuser@example.com",
            first_name="Test",
            last_name="User"
        )
        self.laptop = Laptop.objects.create(
            computer_id="L12345",
            computer_number="LN67890",
            condition="Good",
            status="Checked In",
            checkout_user=self.user
        )

    def test_laptop_creation(self):
        self.assertEqual(self.laptop.computer_id, "L12345")
        self.assertEqual(self.laptop.condition, "Good")
        self.assertEqual(self.laptop.status, "Checked In")
        self.assertEqual(self.laptop.checkout_user, self.user)

    def test_laptop_string_representation(self):
        self.assertEqual(
            str(self.laptop), 
            f"Laptop: {self.laptop.computer_id}, User: {self.laptop.checkout_user}"
        )


class TransactionModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            a_number="A12345678",
            email="testuser@example.com",
            first_name="Test",
            last_name="User"
        )
        self.laptop = Laptop.objects.create(
            computer_id="L12345",
            computer_number="LN67890",
            condition="Good"
        )
        self.transaction = Transaction.objects.create(
            user_id=self.user,
            computer_id=self.laptop,
            condition_out="Good"
        )

    def test_transaction_creation(self):
        self.assertEqual(self.transaction.user_id, self.user)
        self.assertEqual(self.transaction.computer_id, self.laptop)
        self.assertEqual(self.transaction.condition_out, "Good")
        self.assertIsNone(self.transaction.condition_in)  # As it's not yet updated

    def test_transaction_string_representation(self):
        self.assertEqual(
            str(self.transaction), 
            f"#{self.transaction.transaction_id} - User: {self.transaction.user_id} - Laptop: {self.transaction.computer_id}"
        )