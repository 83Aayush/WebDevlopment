"""
Project Title : Contact Management System
Name         : [Your Name]
Date         : 2025
Description  : URL patterns for the contacts app
               Each URL maps to a view function.
               name='...' lets us use {% url 'name' %} in templates.
"""

from django.urls import path
from . import views   # Import all views from this app

urlpatterns = [
    # Home page — list all contacts
    path('', views.index, name='index'),

    # Add a new contact
    path('add/', views.add_contact, name='add_contact'),

    # Edit an existing contact (pk = primary key / ID of the contact)
    path('edit/<int:pk>/', views.edit_contact, name='edit_contact'),

    # Delete a contact
    path('delete/<int:pk>/', views.delete_contact, name='delete_contact'),

    # View full details of one contact
    path('contact/<int:pk>/', views.contact_detail, name='contact_detail'),
]
