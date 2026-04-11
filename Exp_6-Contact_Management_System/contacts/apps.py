"""
Project Title : Contact Management System
Name         : [Your Name]
Date         : 2025
Description  : App configuration for the contacts app.
               Django uses this to identify and configure the app.
"""

from django.apps import AppConfig


class ContactsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contacts'
    verbose_name = 'Contact Management'
