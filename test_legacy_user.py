#!/usr/bin/env python3
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store_project.settings')
django.setup()

from django.db import connections
from accounting.custom_user import LegacyUser

print("Testing LegacyUser model...")

try:
    # Use cursor to avoid ORM issues with last_login
    with connections['legacy'].cursor() as cursor:
        cursor.execute("SELECT Id, Name, Pass, Is_Active, Semat FROM Users")
        user_row = cursor.fetchone()
    
    if user_row:
        # استخراج مقادیر از tuple
        user_id, user_name, stored_pass, is_active, semat = user_row
        
        # ساخت آبجکت LegacyUser
        user = LegacyUser(
            id=user_id,
            name=user_name,
            password=stored_pass,
            is_active=is_active,
            semat=semat
        )
        
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