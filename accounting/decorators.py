# accounting/decorators.py

from functools import wraps
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# ما دیگر نیازی به دکوریتور سفارشی نداریم
# از دکوریتور استاندارد جنگو استفاده می‌کنیم
legacy_login_required = login_required 