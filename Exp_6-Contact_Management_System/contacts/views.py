"""
Project Title : Contact Management System
Name         : [Your Name]
Date         : 2025
Description  : Views (controllers) for the contacts app
               Each function handles one URL/page.
               Views receive a request and return an HTML response.
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages  # For showing success/error messages
from django.db.models import Q       # Q lets us do OR searches in database
from .models import Contact
from .forms import ContactForm


# ─────────────────────────────────────────────────────────────
#  HOME PAGE — Show all contacts (Read Operation)
# ─────────────────────────────────────────────────────────────
def index(request):
    """
    Home page view.
    - Shows all contacts in alphabetical order.
    - Also handles the search feature (Task 7).
    - GET request: just display contacts.
    """

    # Get the search query from URL, e.g. /?q=ravi
    query = request.GET.get('q', '').strip()

    if query:
        # Q objects allow us to search across multiple fields with OR logic
        # icontains = case-insensitive contains (like SQL LIKE '%value%')
        contacts = Contact.objects.filter(
            Q(name__icontains=query) |
            Q(phone__icontains=query) |
            Q(email__icontains=query)
        )
    else:
        # No search — show all contacts
        contacts = Contact.objects.all()

    # Total number of contacts (for stats display)
    total_contacts = Contact.objects.count()

    # Pass data to the template using context dictionary
    context = {
        'contacts': contacts,
        'query': query,
        'total_contacts': total_contacts,
        'result_count': contacts.count(),
    }
    return render(request, 'contacts/index.html', context)


# ─────────────────────────────────────────────────────────────
#  ADD CONTACT — Create Operation
# ─────────────────────────────────────────────────────────────
def add_contact(request):
    """
    Add a new contact.
    - GET request: show the empty form.
    - POST request: validate form data, save to database, redirect to home.
    """

    if request.method == 'POST':
        # Fill form with the submitted data
        form = ContactForm(request.POST)

        if form.is_valid():
            # All validation passed — save to database
            form.save()

            # Show a success flash message
            messages.success(request, f"✅ Contact '{form.cleaned_data['name']}' added successfully!")

            # Redirect to home page — good practice to prevent double-submit
            return redirect('index')
        else:
            # Validation failed — show error message
            messages.error(request, "⚠️ Please fix the errors below and try again.")

    else:
        # GET request — show a blank form
        form = ContactForm()

    context = {
        'form': form,
        'title': 'Add New Contact',
        'btn_text': 'Save Contact',
    }
    return render(request, 'contacts/add_contact.html', context)


# ─────────────────────────────────────────────────────────────
#  EDIT CONTACT — Update Operation
# ─────────────────────────────────────────────────────────────
def edit_contact(request, pk):
    """
    Edit an existing contact.
    - pk (primary key) = unique ID of the contact in the database.
    - GET request: show form pre-filled with existing data.
    - POST request: validate, save updated data, redirect.
    - get_object_or_404: if contact with this pk doesn't exist, show 404 page.
    """

    # Fetch the contact from database, or show 404 if not found
    contact = get_object_or_404(Contact, pk=pk)

    if request.method == 'POST':
        # instance=contact tells Django to UPDATE this record, not create new
        form = ContactForm(request.POST, instance=contact)

        if form.is_valid():
            form.save()
            messages.success(request, f"✏️ Contact '{contact.name}' updated successfully!")
            return redirect('index')
        else:
            messages.error(request, "⚠️ Please fix the errors below and try again.")

    else:
        # Pre-fill the form with existing contact data
        form = ContactForm(instance=contact)

    context = {
        'form': form,
        'contact': contact,
        'title': f'Edit — {contact.name}',
        'btn_text': 'Update Contact',
    }
    return render(request, 'contacts/edit_contact.html', context)


# ─────────────────────────────────────────────────────────────
#  DELETE CONTACT — Delete Operation
# ─────────────────────────────────────────────────────────────
def delete_contact(request, pk):
    """
    Delete a contact.
    - We only delete on POST request (not GET) for security.
      A GET request just shows a confirmation page.
    - After deletion, redirect to home.
    """

    contact = get_object_or_404(Contact, pk=pk)

    if request.method == 'POST':
        name = contact.name   # Save name before deleting for the message
        contact.delete()
        messages.success(request, f"🗑️ Contact '{name}' deleted successfully!")
        return redirect('index')

    # GET request — show confirmation page
    context = {'contact': contact}
    return render(request, 'contacts/delete_confirm.html', context)


# ─────────────────────────────────────────────────────────────
#  VIEW SINGLE CONTACT (Detail Page)
# ─────────────────────────────────────────────────────────────
def contact_detail(request, pk):
    """
    Show full details of a single contact.
    """
    contact = get_object_or_404(Contact, pk=pk)
    context = {'contact': contact}
    return render(request, 'contacts/contact_detail.html', context)
