from django.urls import path

from . import views

urlpatterns = [
    path("", views.actions, name = "actions"),
    path("checkin", views.checkin, name = "checkin"),
    path("create_account", views.create_account, name = "create_account"),
    path("checkout", views.checkout, name = "checkout"),
]