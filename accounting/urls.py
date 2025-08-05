from django.urls import path
from . import views

app_name = 'accounting'

urlpatterns = [
    # Development Dashboard
    path('dev-dashboard/', views.development_dashboard, name='dev_dashboard'),
    
    # Home
    path('', views.home, name='home'),
    
    # Authentication
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Persons
    path('persons/', views.person_list, name='person_list'),
    path('persons/new/', views.person_create, name='person_create'),
    path('persons/<int:person_id>/', views.person_detail, name='person_detail'),
    path('persons/<int:person_id>/edit/', views.person_update, name='person_update'),
    
    # Person Groups
    path('person-groups/', views.person_group_list, name='person_group_list'),
    path('person-groups/new/', views.person_group_create, name='person_group_create'),
    path('person-groups/<int:pk>/edit/', views.person_group_update, name='person_group_update'),
    path('person-groups/<int:pk>/delete/', views.person_group_delete, name='person_group_delete'),
    
    # Goods
    path('goods/', views.good_list, name='good_list'),
    path('goods/new/', views.good_create, name='good_create'),
    path('goods/<int:good_id>/', views.good_detail, name='good_detail'),
    path('goods/<int:good_id>/edit/', views.good_update, name='good_update'),
    path('goods/<int:good_id>/kardex/', views.good_kardex, name='good_kardex'),
    path('goods/<int:good_code>/delete/', views.good_delete, name='good_delete'),
    
    # Good Groups
    path('good-groups/', views.good_group_list, name='good_group_list'),
    path('good-groups/new/', views.good_group_create, name='good_group_create'),
    path('good-groups/<int:pk>/edit/', views.good_group_update, name='good_group_update'),
    path('good-groups/<int:pk>/delete/', views.good_group_delete, name='good_group_delete'),
    
    # Sanads
    path('sanads/', views.sanad_list, name='sanad_list'),
    
    # Stores
    path('stores/', views.store_list, name='store_list'),
    path('stores/new/', views.store_create, name='store_create'),
    path('stores/<int:pk>/edit/', views.store_update, name='store_update'),
    path('stores/<int:pk>/delete/', views.store_delete, name='store_delete'),
    
    # Sandoghs
    path('sandoghs/', views.sandogh_list, name='sandogh_list'),
    path('sandoghs/new/', views.sandogh_create, name='sandogh_create'),
    path('sandoghs/<int:pk>/edit/', views.sandogh_update, name='sandogh_update'),
    path('sandoghs/<int:pk>/delete/', views.sandogh_delete, name='sandogh_delete'),
    
    # Banks
    path('banks/', views.bank_list, name='bank_list'),
    path('banks/new/', views.bank_create, name='bank_create'),
    path('banks/<int:pk>/edit/', views.bank_update, name='bank_update'),
    path('banks/<int:pk>/delete/', views.bank_delete, name='bank_delete'),
    
    # Incomes
    path('incomes/', views.income_list, name='income_list'),
    path('incomes/new/', views.income_create, name='income_create'),
    path('incomes/<int:pk>/edit/', views.income_update, name='income_update'),
    path('incomes/<int:pk>/delete/', views.income_delete, name='income_delete'),
    
    # Expenses
    path('expenses/', views.expense_list, name='expense_list'),
    path('expenses/new/', views.expense_create, name='expense_create'),
    path('expenses/<int:pk>/edit/', views.expense_update, name='expense_update'),
    path('expenses/<int:pk>/delete/', views.expense_delete, name='expense_delete'),
    
    # Fiscal Years
    path('fiscal-years/', views.fiscal_year_list, name='fiscal_year_list'),
    path('fiscal-years/new/', views.fiscal_year_create, name='fiscal_year_create'),
    path('fiscal-years/<int:pk>/edit/', views.fiscal_year_update, name='fiscal_year_update'),
    path('fiscal-years/<int:pk>/delete/', views.fiscal_year_delete, name='fiscal_year_delete'),
    
    # Check Bands
    path('check-bands/', views.check_band_list, name='check_band_list'),
    path('check-bands/new/', views.check_band_create, name='check_band_create'),
    path('check-bands/<int:pk>/edit/', views.check_band_update, name='check_band_update'),
    path('check-bands/<int:pk>/delete/', views.check_band_delete, name='check_band_delete'),
    
    # Company Info
    path('company-info/edit/', views.company_info_update, name='company_info_update'),
    
    # Sales Invoice
    path('sale-invoice/create/', views.sale_invoice_create, name='sale_invoice_create'),
    
    # Reports
    path('reports/inventory/', views.inventory_report, name='inventory_report'),
    path('reports/financial/', views.financial_report, name='financial_report'),
    
    # Development
    path('dev-links/', views.dev_links, name='dev_links'),
    
    # Sales
    path('sales/', views.sales_list, name='sales_list'),
    path('sales/create/', views.sales_create, name='sales_create'),
    path('sales/<int:sale_id>/', views.sales_detail, name='sales_detail'),
    path('create-sale-invoice/', views.create_sale_invoice, name='create_sale_invoice'),
    
    # Purchases
    path('purchases/', views.purchase_list, name='purchase_list'),
    path('purchases/create/', views.purchase_create, name='purchase_create'),
    
    # Cheques
    path('cheques/receive/', views.cheque_receive_list, name='cheque_receive_list'),
    path('cheques/receive/create/', views.cheque_receive_create, name='cheque_receive_create'),
    path('cheques/receive/<int:cheque_id>/status/', views.cheque_receive_status_update, name='cheque_receive_status_update'),
    path('cheques/pay/', views.cheque_pay_list, name='cheque_pay_list'),
    path('cheques/pay/create/', views.cheque_pay_create, name='cheque_pay_create'),
    
    # Dynamic Lists
    path('dynamic/sales/', views.sales_list_dynamic, name='sales_list_dynamic'),
    path('dynamic/purchases/', views.purchase_list_dynamic, name='purchase_list_dynamic'),
    path('dynamic/sanads/', views.sanad_list_dynamic, name='sanad_list_dynamic'),
    path('dynamic/goods/', views.good_list_dynamic, name='good_list_dynamic'),
    
    # Database
    path('upload-bak/', views.upload_bak, name='upload_bak'),
    path('backup-db/', views.backup_db, name='backup_db'),
    path('sanads/<int:sanad_id>/', views.sanad_detail, name='sanad_detail'),
    
    # Users
    path('users/', views.user_list, name='user_list'),
    path('debug-passwords/', views.debug_passwords, name='debug_passwords'),
    path('test-password-formats/', views.test_password_formats, name='test_password_formats'),
    path('export-users-passwords/', views.export_users_passwords, name='export_users_passwords'),
    
    # API endpoints
    path('api/good-info/', views.get_good_info, name='get_good_info'),
    path('api/person-info/', views.get_person_info, name='get_person_info'),
    path('person-settings/', views.person_settings, name='person_settings'),
] 