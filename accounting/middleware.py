from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # صفحاتی که نیاز به لاگین ندارند
        exempt_urls = [
            '/login/',
            '/admin/',
            '/static/',
            '/media/',
        ]
        
        # بررسی اینکه آیا URL فعلی از لاگین معاف است
        current_path = request.path_info
        is_exempt = any(current_path.startswith(url) for url in exempt_urls)
        
        # اگر صفحه معاف نیست و کاربر لاگین نکرده، به صفحه لاگین هدایت کن
        if not is_exempt and not request.user.is_authenticated:
            return redirect('login')
        
        response = self.get_response(request)
        return response 