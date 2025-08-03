# accounting/decorators.py

from functools import wraps
from django.shortcuts import redirect
from django.contrib.auth import SESSION_KEY
from .authentication import LegacyDBBackend

def legacy_login_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # === دستور دیباگ ===
        print(f"DEBUG: legacy_login_required called for {view_func.__name__}")
        print(f"DEBUG: request.user.is_authenticated = {request.user.is_authenticated}")
        print(f"DEBUG: SESSION_KEY in request.session = {SESSION_KEY in request.session}")
        # ===================
        
        # آیا کلید session کاربر وجود دارد؟
        if SESSION_KEY in request.session:
            user_id = request.session[SESSION_KEY]
            print(f"DEBUG: user_id from session = {user_id}")
            # تلاش برای گرفتن کاربر با استفاده از بکند سفارشی ما
            backend = LegacyDBBackend()
            user = backend.get_user(user_id)
            
            # اگر کاربر معتبر و فعال پیدا شد
            if user and user.is_active:
                print(f"DEBUG: User found and active: {user.name}")
                # کاربر را به request اضافه می‌کنیم تا در ویو قابل دسترس باشد
                request.user = user
                return view_func(request, *args, **kwargs)
            else:
                print(f"DEBUG: User not found or not active")
        else:
            print(f"DEBUG: No SESSION_KEY in session")
        
        # اگر هیچکدام از شرایط بالا برقرار نبود، به صفحه لاگین هدایت کن
        print(f"DEBUG: Redirecting to login")
        return redirect('accounting:login')

    return _wrapped_view 