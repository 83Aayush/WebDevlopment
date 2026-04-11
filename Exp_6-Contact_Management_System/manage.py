#!/usr/bin/env python
"""
Project Title : Contact Management System
Name         : [Your Name]
Date         : 2025
Description  : Django management script — entry point for all Django commands
"""

import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'contact_management_system.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Make sure it is installed and "
            "available on your PYTHONPATH environment variable."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
