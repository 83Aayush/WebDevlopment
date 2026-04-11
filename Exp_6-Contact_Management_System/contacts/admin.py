"""
Project Title : Contact Management System
Name         : [Your Name]
Date         : 2025
Description  : Register Contact model with Django Admin panel
               After registering, you can manage contacts at /admin/
"""

from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Customize how Contact appears in the Django Admin panel.
    This is optional but makes the admin much more usable.
    """

    # Columns to show in the list view
    list_display = ('name', 'phone', 'email', 'created_at')

    # Add a search box in admin
    search_fields = ('name', 'phone', 'email')

    # Add filter sidebar
    list_filter = ('created_at',)

    # Make the list sortable by name
    ordering = ('name',)
