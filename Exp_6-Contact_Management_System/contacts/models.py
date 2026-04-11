"""
Project Title : Contact Management System
Name         : [Your Name]
Date         : 2025
Description  : Database models for the contacts app
               A Model in Django is like a blueprint for a database table.
               Each attribute = one column in the table.
"""

from django.db import models


class Contact(models.Model):
    """
    Contact model — stores all information about one contact person.
    Django will automatically create a table called 'contacts_contact'
    in the database when we run migrations.
    """

    # Name of the contact — max 100 characters
    name = models.CharField(max_length=100)

    # Phone number — stored as text so leading zeros are not lost
    phone = models.CharField(max_length=15)

    # Email address — Django validates email format automatically
    email = models.EmailField()

    # Optional address field — blank=True means it is not required
    address = models.TextField(blank=True, null=True)

    # Automatically saves the date & time when a contact is created
    created_at = models.DateTimeField(auto_now_add=True)

    # Automatically saves the date & time whenever a contact is updated
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # This controls how a contact is shown in admin & debug output
        return self.name

    class Meta:
        # Sort contacts alphabetically by name by default
        ordering = ['name']
