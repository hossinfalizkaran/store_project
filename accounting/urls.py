from django.urls import path
from . import views

app_name = 'accounting'

urlpatterns = [
    # ========================================
    # URL های اصلی
    # ========================================
    path('', views.home, name='home'),
    path('dev-links/', views.dev_links, name='dev_links'),
    
    # ========================================
    # URL های احراز هویت
    # ========================================
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # ========================================
    # URL های مدیریت کاربران
    # ========================================
    path('users/', views.user_list, name='user_list'),
    path('debug-passwords/', views.debug_passwords, name='debug_passwords'),
    path('test-passwords/', views.test_password_formats, name='test_password_formats'),
    path('export-users/', views.export_users_passwords, name='export_users'),
    
    # ========================================
    # URL های مدیریت فایل و پشتیبان‌گیری
    # ========================================
    path('upload-bak/', views.upload_bak, name='upload_bak'),
    path('backup-db/', views.backup_db, name='backup_db'),
    
    # ========================================
    # URL های اسناد حسابداری
    # ========================================
    path('sanads/', views.sanad_list, name='sanad_list'),
    path('sanads/<int:sanad_id>/', views.sanad_detail, name='sanad_detail'),
    
    # ========================================
    # URL های فروش
    # ========================================
    path('sales/', views.sales_list, name='sales_list'),
    path('sales/create/', views.sales_create, name='sales_create'),
    path('sales/create-invoice/', views.create_sale_invoice, name='create_sale_invoice'),
    path('sales/<int:sale_id>/', views.sales_detail, name='sales_detail'),
    
    # ========================================
    # URL های خرید
    # ========================================
    path('purchase/', views.purchase_list, name='purchase_list'),
    path('purchase/create/', views.purchase_create, name='purchase_create'),
    
    # ========================================
    # URL های چک دریافتی
    # ========================================
    path('cheque/receive/', views.cheque_receive_list, name='cheque_receive_list'),
    path('cheque/receive/create/', views.cheque_receive_create, name='cheque_receive_create'),
    path('cheque/receive/<int:cheque_id>/status/', views.cheque_receive_status_update, name='cheque_receive_status_update'),
    
    # ========================================
    # URL های چک پرداختی
    # ========================================
    path('cheque/pay/', views.cheque_pay_list, name='cheque_pay_list'),
    path('cheque/pay/create/', views.cheque_pay_create, name='cheque_pay_create'),
    
    # ========================================
    # URL های گزارش‌گیری
    # ========================================
    path('reports/inventory/', views.inventory_report, name='inventory_report'),
    path('reports/financial/', views.financial_report, name='financial_report'),
    
    # ========================================
    # URL های API برای AJAX
    # ========================================
    path('api/good-info/', views.get_good_info, name='get_good_info'),
    path('api/person-info/', views.get_person_info, name='get_person_info'),

    # ========================================
    # URL های اشخاص
    # ========================================
    path('person/list/', views.person_list, name='person_list'),
    path('person/settings/', views.person_settings, name='person_settings'),
    path('person/create/', views.person_create, name='person_create'),
    path('person/<int:person_id>/', views.person_detail, name='person_detail'),
    path('person/<int:person_id>/edit/', views.person_update, name='person_update'),
    
    # ========================================
    # URL های کالاها
    # ========================================
    path('goods/', views.good_list, name='good_list'),
    path('goods/new/', views.good_create, name='good_create'),
    path('goods/<int:good_id>/', views.good_detail, name='good_detail'),
    path('goods/<int:good_id>/edit/', views.good_update, name='good_update'),
    path('goods/<int:good_id>/delete/', views.good_delete, name='good_delete'),
    
    # ========================================
    # URL های مدیریت اطلاعات پایه
    # ========================================
    
    # انبارها
    path('stores/', views.store_list, name='store_list'),
    path('stores/create/', views.store_create, name='store_create'),
    path('stores/<int:pk>/edit/', views.store_update, name='store_update'),
    path('stores/<int:pk>/delete/', views.store_delete, name='store_delete'),
    
    # صندوق‌ها
    path('sandoghs/', views.sandogh_list, name='sandogh_list'),
    path('sandoghs/create/', views.sandogh_create, name='sandogh_create'),
    path('sandoghs/<int:pk>/edit/', views.sandogh_update, name='sandogh_update'),
    path('sandoghs/<int:pk>/delete/', views.sandogh_delete, name='sandogh_delete'),
    
    # بانک‌ها
    path('banks/', views.bank_list, name='bank_list'),
    path('banks/create/', views.bank_create, name='bank_create'),
    path('banks/<int:pk>/edit/', views.bank_update, name='bank_update'),
    path('banks/<int:pk>/delete/', views.bank_delete, name='bank_delete'),
    
    # درآمدها
    path('incomes/', views.income_list, name='income_list'),
    path('incomes/create/', views.income_create, name='income_create'),
    path('incomes/<int:pk>/edit/', views.income_update, name='income_update'),
    path('incomes/<int:pk>/delete/', views.income_delete, name='income_delete'),
    
    # هزینه‌ها
    path('expenses/', views.expense_list, name='expense_list'),
    path('expenses/create/', views.expense_create, name='expense_create'),
    path('expenses/<int:pk>/edit/', views.expense_update, name='expense_update'),
    path('expenses/<int:pk>/delete/', views.expense_delete, name='expense_delete'),
    
    # دوره‌های مالی
    path('fiscal-years/', views.fiscal_year_list, name='fiscal_year_list'),
    path('fiscal-years/create/', views.fiscal_year_create, name='fiscal_year_create'),
    path('fiscal-years/<int:pk>/edit/', views.fiscal_year_update, name='fiscal_year_update'),
    path('fiscal-years/<int:pk>/delete/', views.fiscal_year_delete, name='fiscal_year_delete'),
    
    # دسته چک‌ها
    path('check-bands/', views.check_band_list, name='check_band_list'),
    path('check-bands/create/', views.check_band_create, name='check_band_create'),
    path('check-bands/<int:pk>/edit/', views.check_band_update, name='check_band_update'),
    path('check-bands/<int:pk>/delete/', views.check_band_delete, name='check_band_delete'),
    
    # مشخصات شرکت
    path('company-info/edit/', views.company_info_update, name='company_info_update'),
    
    # لیست‌های داینامیک با تنظیمات UI
    path('sales/list-dynamic/', views.sales_list_dynamic, name='sales_list_dynamic'),
    path('purchase/list-dynamic/', views.purchase_list_dynamic, name='purchase_list_dynamic'),
    path('sanad/list-dynamic/', views.sanad_list_dynamic, name='sanad_list_dynamic'),
    path('good/list-dynamic/', views.good_list_dynamic, name='good_list_dynamic'),
    
    # ========================================
    # URL های فاکتور فروش
    # ========================================
    path('sale-invoice/create/', views.sale_invoice_create, name='sale_invoice_create'),
] 