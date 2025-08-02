from django.urls import path
from . import views

app_name = 'accounting'

urlpatterns = [
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