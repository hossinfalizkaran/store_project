#!/usr/bin/env python3
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store_project.settings')
django.setup()

from accounting.models import LegacyUser

print("Testing LegacyUser model...")

try:
    # Try to get the first user
    user = LegacyUser.objects.using('legacy').first()
    
    if user:
        print(f"Found user: {user.name}")
        print(f"User ID: {user.id}")
        print(f"Password field: {user.password}")
        print(f"Is active: {user.is_active}")
        print(f"Semat: {user.semat}")
    else:
        print("No users found in database")
        
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc() 