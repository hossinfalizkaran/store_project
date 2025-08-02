"""
URL configuration for store_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from accounting import views as accounting_views

urlpatterns = [
    path('', accounting_views.home, name='home'),
    path('admin/', admin.site.urls),

    # صفحات اصلی
    path('dev-links/', accounting_views.dev_links, name='dev_links'),
    
    # مدیریت فایل و پشتیبان‌گیری
    path('upload-bak/', accounting_views.upload_bak, name='upload_bak'),
    path('backup-db/', accounting_views.backup_db, name='backup_db'),
    
    # اسناد حسابداری
    path('sanads/', accounting_views.sanad_list, name='sanad_list'),
    path('sanads/<int:sanad_id>/', accounting_views.sanad_detail, name='sanad_detail'),
    
    # مدیریت اشخاص
    path('persons/', accounting_views.person_list, name='person_list'),
    path('persons/new/', accounting_views.person_create, name='person_create'),
    path('persons/<int:person_id>/', accounting_views.person_detail, name='person_detail'),
    path('persons/<int:person_id>/edit/', accounting_views.person_update, name='person_update'),
    path('persons/settings/', accounting_views.person_settings, name='person_settings'),
    
    # مدیریت کالاها
    path('goods/', accounting_views.good_list, name='good_list'),
    path('goods/new/', accounting_views.good_create, name='good_create'),
    path('goods/<int:good_id>/', accounting_views.good_detail, name='good_detail'),
    path('goods/<int:good_id>/edit/', accounting_views.good_update, name='good_update'),
    
    # مدیریت فروش
    path('sales/', accounting_views.sales_list_dynamic, name='sales_list'),
    path('sales/create/', accounting_views.create_sale_invoice, name='create_sale_invoice'),
    path('sales/<int:sale_id>/', accounting_views.sales_detail, name='sales_detail'),
    path('sale-invoice/create/', accounting_views.sale_invoice_create, name='sale_invoice_create'),
    
    # مدیریت خرید
    path('purchases/', accounting_views.purchase_list_dynamic, name='purchase_list'),
    path('purchases/create/', accounting_views.purchase_create, name='purchase_create'),
]

urlpatterns += [
    # احراز هویت
    path('login/', accounting_views.login_view, name='login'),
    path('logout/', accounting_views.logout_view, name='logout'),
    
    # مدیریت کاربران
    path('users/', accounting_views.user_list, name='user_list'),
    path('debug-passwords/', accounting_views.debug_passwords, name='debug_passwords'),
    path('test-passwords/', accounting_views.test_password_formats, name='test_password_formats'),
    path('export-users/', accounting_views.export_users_passwords, name='export_users'),
]

# اضافه کردن فایل‌های استاتیک در حالت DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
