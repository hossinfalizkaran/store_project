# accounting/decorators.py

from functools import wraps
from django.shortcuts import redirect
from django.contrib.auth import SESSION_KEY
from .authentication import LegacyDBBackend

def legacy_login_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # آیا کلید session کاربر وجود دارد؟
        if SESSION_KEY in request.session:
            user_id = request.session[SESSION_KEY]
            # تلاش برای گرفتن کاربر با استفاده از بکند سفارشی ما
            backend = LegacyDBBackend()
            user = backend.get_user(user_id)
            
            # اگر کاربر معتبر و فعال پیدا شد
            if user and user.is_active:
                # کاربر را به request اضافه می‌کنیم تا در ویو قابل دسترس باشد
                request.user = user
                return view_func(request, *args, **kwargs)
        
        # اگر هیچکدام از شرایط بالا برقرار نبود، به صفحه لاگین هدایت کن
        return redirect('accounting:login')

    return _wrapped_view 