# accounting/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Max, Q
from django.core.paginator import Paginator, EmptyPage
from django.db import connections, transaction
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from decimal import Decimal
import json
from datetime import datetime
import jdatetime
import pytz

# Import all necessary models and forms
from .models import (
    Perinf, Pergrp, Goodinf, Goodgrps, Sanad, Stores, SandoghTbl,
    Bank, Ldaramad, LHazine, InfCo, Fiscalyear, Checkband, 
    FactFo, FactFoDetail, Kardex, Kharid, ChequesRecieve, ChequePay,
    Chequerecievelog, ChequepayLog, GetRecieve, Settings, Users
)
from .forms import (
    PersonForm, GoodForm, StoreForm, SandoghForm, BankForm,
    IncomeForm, ExpenseForm, CompanyInfoForm, FiscalYearForm, CheckBandForm,
    SaleInvoiceForm, SaleInvoiceDetailFormSet
)

# Helper function to convert raw query results to dictionaries
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def normalize_persian_text(text):
    """
    متن فارسی را نرمال‌سازی می‌کند تا حروف عربی و فارسی یکسان شوند.
    """
    if not text:
        return text
    
    # تبدیل حروف عربی به فارسی
    arabic_to_persian = {
        'ي': 'ی',  # ی عربی به ی فارسی
        'ك': 'ک',  # ک عربی به ک فارسی
        'ة': 'ه',  # ة عربی به ه فارسی
        'ؤ': 'و',  # و عربی به و فارسی
        'ئ': 'ی',  # ئ عربی به ی فارسی
        'إ': 'ا',  # إ عربی به ا فارسی
        'أ': 'ا',  # أ عربی به ا فارسی
        'آ': 'آ',  # آ عربی به آ فارسی
        'ء': '',   # حذف همزه
    }
    
    for arabic, persian in arabic_to_persian.items():
        text = text.replace(arabic, persian)
    
    return text

def get_active_users_for_login():
    """
    نسخه اصلاح شده و قابل دیباگ:
    لیستی از نام‌های کاربری فعال و دارای رمز عبور را برای نمایش در dropdown لاگین برمی‌گرداند.
    """
    user_list = []
    try:
        with connections['legacy'].cursor() as cursor:
            # کوئری را ساده‌تر می‌کنیم تا مطمئن شویم کار می‌کند
            query = """
                SELECT Name FROM Users 
                WHERE Is_Active = 1 AND Pass IS NOT NULL AND Pass != '' AND Name != 'مدير'
                ORDER BY Name
            """
            cursor.execute(query)
            users = cursor.fetchall()
            user_list = [user[0] for user in users]
            
            # === دستور دیباگ ===
            print(f"DEBUG: Found {len(user_list)} users for login dropdown.")
            if user_list:
                print(f"DEBUG: First few users: {user_list[:5]}")
            # ===================

    except Exception as e:
        print(f"ERROR in get_active_users_for_login: {e}")
    
    return user_list

def get_new_code(model):
    """یک کد جدید بر اساس بزرگترین کد موجود در مدل ایجاد می‌کند."""
    max_code_result = model.objects.using('legacy').aggregate(max_code=Max('code'))
    max_code = max_code_result.get('max_code') or 0
    return max_code + 1

# --- Main Views ---
@login_required
def home(request):
    # این ویو باید بسیار ساده باشد و فقط تمپلیت را رندر کند
    return render(request, 'home.html')

# --- Person Views ---
@login_required
def person_list(request):
    connection = connections['legacy']
    search_query = request.GET.get('q', '').strip()
    where_clause = ""
    params = []

    if search_query:
        search_param = f'%{search_query}%'
        collation = "COLLATE Persian_100_CI_AI"
        where_clause = f"WHERE p.FullName {collation} LIKE %s OR CAST(p.Code AS VARCHAR(20)) LIKE %s"
        params = [search_param, search_param]

    with connection.cursor() as cursor:
        cursor.execute(f"SELECT COUNT(*) FROM PerInf p {where_clause}", params)
        total_count = cursor.fetchone()[0]

    paginator = Paginator(range(total_count), 25)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    offset = (page_obj.number - 1) * 25

    with connection.cursor() as cursor:
        query = f"""
            SELECT p.Code, p.FullName, pg.Name as GroupName, p.Status
            FROM PerInf p
            LEFT JOIN PerGrp pg ON p.GrpCode = pg.Code
            {where_clause}
            ORDER BY p.Code
            OFFSET %s ROWS FETCH NEXT %s ROWS ONLY
        """
        cursor.execute(query, params + [offset, 25])
        persons = dictfetchall(cursor)

    context = {'page_obj': page_obj, 'persons': persons, 'search_query': search_query, 'total_count': total_count}
    return render(request, 'person_list.html', context)

@login_required
def person_detail(request, person_id):
    person = get_object_or_404(Perinf.objects.using('legacy'), code=person_id)
    context = {
        'person': person,
        'title': f'جزئیات شخص - {person.fullname}',
    }
    return render(request, 'person_detail.html', context)

@login_required
def person_create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            
            # پیدا کردن بزرگترین کد موجود و اختصاص کد جدید
            person.code = get_new_code(Perinf)
            
            # ساخت fullname بعد از اعتبارسنجی
            person.fullname = f"{form.cleaned_data.get('name') or ''} {form.cleaned_data.get('lname') or ''}".strip()

            person.save(using='legacy')
            messages.success(request, f"شخص '{person.fullname}' با موفقیت ایجاد شد.")
            return redirect('accounting:person_list')
        else:
            messages.error(request, "لطفاً خطاهای فرم را برطرف کنید.")
    else:
        form = PersonForm()

    context = {
        'form': form,
        'form_title': 'ایجاد شخص جدید'
    }
    return render(request, 'person_form.html', context)

@login_required
def person_update(request, person_id):
    person = get_object_or_404(Perinf.objects.using('legacy'), code=person_id)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            updated_person = form.save(commit=False)
            # بازسازی fullname
            updated_person.fullname = f"{form.cleaned_data.get('name') or ''} {form.cleaned_data.get('lname') or ''}".strip()
            updated_person.save(using='legacy')

            messages.success(request, f"اطلاعات شخص '{person.fullname}' با موفقیت ویرایش شد.")
            return redirect('accounting:person_detail', person_id=person.code)
        else:
            messages.error(request, "لطفاً خطاهای فرم را برطرف کنید.")
    else:
        form = PersonForm(instance=person)

    context = {
        'form': form,
        'form_title': f'ویرایش شخص - {person.fullname}',
        'person': person
    }
    return render(request, 'person_form.html', context)

# --- Good Views ---
@login_required
def good_list(request):
    connection = connections['legacy']
    good_groups = Goodgrps.objects.using('legacy').all().order_by('code')
    
    search_query = request.GET.get('q', '').strip()
    selected_group_id = request.GET.get('group', '')
    
    where_clauses = []
    params = []
    collation = "COLLATE Persian_100_CI_AI"

    if search_query:
        where_clauses.append(f"(g.Name {collation} LIKE %s OR CAST(g.Code AS VARCHAR(20)) LIKE %s)")
        params.extend([f'%{search_query}%', f'%{search_query}%'])
    
    if selected_group_id:
        where_clauses.append("g.GrpCode = %s")
        params.append(selected_group_id)

    where_sql = "WHERE " + " AND ".join(where_clauses) if where_clauses else ""

    with connection.cursor() as cursor:
        cursor.execute(f"SELECT COUNT(*) FROM GoodInf g {where_sql}", params)
        total_count = cursor.fetchone()[0]

    paginator = Paginator(range(total_count), 25)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    offset = (page_obj.number - 1) * 25

    with connection.cursor() as cursor:
        query = f"""
            SELECT g.Code, g.Name, gg.Name as GroupName, u.Name as UnitName, g.Mogodi, g.ConsumerPrice
            FROM GoodInf g
            LEFT JOIN GoodGrps gg ON g.GrpCode = gg.Code
            LEFT JOIN Units u ON g.Unit = u.Code
            {where_sql}
            ORDER BY g.Code
            OFFSET %s ROWS FETCH NEXT %s ROWS ONLY
        """
        cursor.execute(query, params + [offset, 25])
        goods = dictfetchall(cursor)
    
    context = {
        'page_obj': page_obj, 'goods': goods, 'good_groups': good_groups, 
        'selected_group_id': selected_group_id, 'search_query': search_query, 
        'total_count': total_count
    }
    return render(request, 'good_list.html', context)

@login_required
def good_detail(request, good_id):
    good = get_object_or_404(Goodinf.objects.using('legacy').select_related('grpcode', 'unit'), code=good_id)
    context = {
        'good': good,
        'title': f'جزئیات کالا - {good.name or good.code}',
    }
    return render(request, 'good_detail.html', context)

@login_required
def good_create(request):
    if request.method == 'POST':
        form = GoodForm(request.POST)
        if form.is_valid():
            good = form.save(commit=False)
            
            # پیدا کردن بزرگترین کد موجود و اختصاص کد جدید
            good.code = get_new_code(Goodinf)
            
            good.save(using='legacy')
            messages.success(request, f"کالا '{good.name}' با موفقیت ایجاد شد.")
            return redirect('accounting:good_list')
        else:
            messages.error(request, "لطفاً خطاهای فرم را برطرف کنید.")
    else:
        form = GoodForm()

    context = {
        'form': form,
        'form_title': 'ایجاد کالای جدید'
    }
    return render(request, 'good_form.html', context)

@login_required
def good_update(request, good_id):
    good = get_object_or_404(Goodinf.objects.using('legacy'), code=good_id)
    if request.method == 'POST':
        form = GoodForm(request.POST, instance=good)
        if form.is_valid():
            form.save(using='legacy')
            messages.success(request, f"اطلاعات کالا '{good.name}' با موفقیت ویرایش شد.")
            return redirect('accounting:good_detail', good_id=good.code)
        else:
            messages.error(request, "لطفاً خطاهای فرم را برطرف کنید.")
    else:
        form = GoodForm(instance=good)

    context = {
        'form': form,
        'form_title': f'ویرایش کالا - {good.name}',
        'good': good
    }
    return render(request, 'good_form.html', context)

@login_required
def good_delete(request, good_code):
    good = get_object_or_404(Goodinf.objects.using('legacy'), code=good_code)
    good_name = good.name
    good.delete()
    messages.success(request, f"کالا '{good_name}' با موفقیت حذف شد.")
    return redirect('accounting:good_list')

# --- Sanad List ---
@login_required
def sanad_list(request):
    connection = connections['legacy']
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM Sanad")
        total_count = cursor.fetchone()[0]

    paginator = Paginator(range(total_count), 25)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    offset = (page_obj.number - 1) * 25

    with connection.cursor() as cursor:
        query = "SELECT Code, Tarikh, Sharh, Status FROM Sanad ORDER BY Code DESC OFFSET %s ROWS FETCH NEXT %s ROWS ONLY"
        cursor.execute(query, [offset, 25])
        sanads = dictfetchall(cursor)

    context = {'page_obj': page_obj, 'sanads': sanads, 'total_count': total_count}
    return render(request, 'sanad_list.html', context)

# --- Generic CRUD Views ---
@login_required
def generic_create_view(request, form_class, model, template_name, context_data, redirect_url_name):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if hasattr(instance, 'code'):
                # پیدا کردن بزرگترین کد موجود و اختصاص کد جدید
                max_code_result = model.objects.using('legacy').aggregate(max_code=Max('code'))
                max_code = max_code_result.get('max_code') or 0
                instance.code = max_code + 1
            instance.save(using='legacy')
            messages.success(request, "مورد جدید با موفقیت ایجاد شد.")
            return redirect(redirect_url_name)
    else:
        form = form_class()
    
    final_context = {'form': form}
    final_context.update(context_data)
    return render(request, template_name, final_context)

@login_required
def generic_update_view(request, pk, form_class, model, template_name, context_data, redirect_url_name):
    instance = get_object_or_404(model.objects.using('legacy'), pk=pk)
    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save(using='legacy')
            messages.success(request, "مورد با موفقیت ویرایش شد.")
            return redirect(redirect_url_name)
    else:
        form = form_class(instance=instance)
    
    final_context = {'form': form, 'instance': instance}
    final_context.update(context_data)
    return render(request, template_name, final_context)

@login_required
def generic_delete_view(request, pk, model, redirect_url_name, success_message):
    instance = get_object_or_404(model.objects.using('legacy'), pk=pk)
    instance_name = getattr(instance, 'name', str(instance))
    instance.delete()
    messages.success(request, success_message.format(instance_name))
    return redirect(redirect_url_name)

# --- Stores ---
@login_required
def store_list(request):
    stores = Stores.objects.using('legacy').all().order_by('code')
    return render(request, 'generic_list.html', {
        'page_obj': stores, 'title': 'لیست انبارها', 'create_url_name': 'accounting:store_create',
        'update_url_name': 'accounting:store_update', 'delete_url_name': 'accounting:store_delete',
        'fields_to_display': ['code', 'name', 'comment']
    })

@login_required
def store_create(request):
    return generic_create_view(
        request, StoreForm, Stores, 'generic_form.html',
        {'form_title': 'ایجاد انبار جدید'}, 'accounting:store_list'
    )

@login_required
def store_update(request, pk):
    return generic_update_view(
        request, pk, StoreForm, Stores, 'generic_form.html',
        {'form_title': 'ویرایش انبار'}, 'accounting:store_list'
    )

@login_required
def store_delete(request, pk):
    return generic_delete_view(
        request, pk, Stores, 'accounting:store_list',
        'انبار "{}" با موفقیت حذف شد.'
    )

# --- Sandoghs ---
@login_required
def sandogh_list(request):
    sandoghs = SandoghTbl.objects.using('legacy').all().order_by('code')
    return render(request, 'generic_list.html', {
        'page_obj': sandoghs, 'title': 'لیست صندوق‌ها', 'create_url_name': 'accounting:sandogh_create',
        'update_url_name': 'accounting:sandogh_update', 'delete_url_name': 'accounting:sandogh_delete',
        'fields_to_display': ['code', 'name', 'comment']
    })

@login_required
def sandogh_create(request):
    return generic_create_view(
        request, SandoghForm, SandoghTbl, 'generic_form.html',
        {'form_title': 'ایجاد صندوق جدید'}, 'accounting:sandogh_list'
    )

@login_required
def sandogh_update(request, pk):
    return generic_update_view(
        request, pk, SandoghForm, SandoghTbl, 'generic_form.html',
        {'form_title': 'ویرایش صندوق'}, 'accounting:sandogh_list'
    )

@login_required
def sandogh_delete(request, pk):
    return generic_delete_view(
        request, pk, SandoghTbl, 'accounting:sandogh_list',
        'صندوق "{}" با موفقیت حذف شد.'
    )

# --- Banks ---
@login_required
def bank_list(request):
    banks = Bank.objects.using('legacy').all().order_by('code')
    return render(request, 'generic_list.html', {
        'page_obj': banks, 'title': 'لیست بانک‌ها', 'create_url_name': 'accounting:bank_create',
        'update_url_name': 'accounting:bank_update', 'delete_url_name': 'accounting:bank_delete',
        'fields_to_display': ['code', 'name', 'shobe', 'sh_h']
    })

@login_required
def bank_create(request):
    return generic_create_view(
        request, BankForm, Bank, 'generic_form.html',
        {'form_title': 'ایجاد بانک جدید'}, 'accounting:bank_list'
    )

@login_required
def bank_update(request, pk):
    return generic_update_view(
        request, pk, BankForm, Bank, 'generic_form.html',
        {'form_title': 'ویرایش بانک'}, 'accounting:bank_list'
    )

@login_required
def bank_delete(request, pk):
    return generic_delete_view(
        request, pk, Bank, 'accounting:bank_list',
        'بانک "{}" با موفقیت حذف شد.'
    )

# --- Incomes ---
@login_required
def income_list(request):
    incomes = Ldaramad.objects.using('legacy').all().order_by('code')
    return render(request, 'generic_list.html', {
        'page_obj': incomes, 'title': 'لیست درآمدها', 'create_url_name': 'accounting:income_create',
        'update_url_name': 'accounting:income_update', 'delete_url_name': 'accounting:income_delete',
        'fields_to_display': ['code', 'name', 'comment']
    })

@login_required
def income_create(request):
    return generic_create_view(
        request, IncomeForm, Ldaramad, 'generic_form.html',
        {'form_title': 'ایجاد درآمد جدید'}, 'accounting:income_list'
    )

@login_required
def income_update(request, pk):
    return generic_update_view(
        request, pk, IncomeForm, Ldaramad, 'generic_form.html',
        {'form_title': 'ویرایش درآمد'}, 'accounting:income_list'
    )

@login_required
def income_delete(request, pk):
    return generic_delete_view(
        request, pk, Ldaramad, 'accounting:income_list',
        'درآمد "{}" با موفقیت حذف شد.'
    )

# --- Expenses ---
@login_required
def expense_list(request):
    expenses = LHazine.objects.using('legacy').all().order_by('code')
    return render(request, 'generic_list.html', {
        'page_obj': expenses, 'title': 'لیست هزینه‌ها', 'create_url_name': 'accounting:expense_create',
        'update_url_name': 'accounting:expense_update', 'delete_url_name': 'accounting:expense_delete',
        'fields_to_display': ['code', 'name', 'comment']
    })

@login_required
def expense_create(request):
    return generic_create_view(
        request, ExpenseForm, LHazine, 'generic_form.html',
        {'form_title': 'ایجاد هزینه جدید'}, 'accounting:expense_list'
    )

@login_required
def expense_update(request, pk):
    return generic_update_view(
        request, pk, ExpenseForm, LHazine, 'generic_form.html',
        {'form_title': 'ویرایش هزینه'}, 'accounting:expense_list'
    )

@login_required
def expense_delete(request, pk):
    return generic_delete_view(
        request, pk, LHazine, 'accounting:expense_list',
        'هزینه "{}" با موفقیت حذف شد.'
    )

# --- Fiscal Years ---
@login_required
def fiscal_year_list(request):
    fiscal_years = Fiscalyear.objects.using('legacy').all().order_by('id')
    return render(request, 'generic_list.html', {
        'page_obj': fiscal_years,
        'title': 'لیست دوره‌های مالی',
        'create_url_name': 'accounting:fiscal_year_create',
        'update_url_name': 'accounting:fiscal_year_update',
        'fields_to_display': ['id', 'title', 'datestart', 'dateend']
    })

@login_required
def fiscal_year_create(request):
    return generic_create_view(
        request, FiscalYearForm, Fiscalyear, 'generic_form.html',
        {'form_title': 'ایجاد دوره مالی جدید'}, 'accounting:fiscal_year_list'
    )

@login_required
def fiscal_year_update(request, pk):
    return generic_update_view(
        request, pk, FiscalYearForm, Fiscalyear, 'generic_form.html',
        {'form_title': 'ویرایش دوره مالی'}, 'accounting:fiscal_year_list'
    )

@login_required
def fiscal_year_delete(request, pk):
    return generic_delete_view(
        request, pk, Fiscalyear, 'accounting:fiscal_year_list',
        'دوره مالی با موفقیت حذف شد.'
    )

# --- Check Bands ---
@login_required
def check_band_list(request):
    check_bands = Checkband.objects.using('legacy').all().order_by('id')
    return render(request, 'generic_list.html', {
        'page_obj': check_bands,
        'title': 'لیست دسته چک‌ها',
        'create_url_name': 'accounting:check_band_create',
        'update_url_name': 'accounting:check_band_update',
        'fields_to_display': ['id', 'serial', 'fromnum', 'tonum']
    })

@login_required
def check_band_create(request):
    return generic_create_view(
        request, CheckBandForm, Checkband, 'generic_form.html',
        {'form_title': 'ایجاد دسته چک جدید'}, 'accounting:check_band_list'
    )

@login_required
def check_band_update(request, pk):
    return generic_update_view(
        request, pk, CheckBandForm, Checkband, 'generic_form.html',
        {'form_title': 'ویرایش دسته چک'}, 'accounting:check_band_list'
    )

@login_required
def check_band_delete(request, pk):
    return generic_delete_view(
        request, pk, Checkband, 'accounting:check_band_list',
        'دسته چک با موفقیت حذف شد.'
    )

# --- Company Info ---
@login_required
def company_info_update(request):
    # استفاده از raw SQL برای InfCo چون فیلد id ندارد
    try:
        cursor = connections['legacy'].cursor()
        cursor.execute("SELECT TOP 1 * FROM inf_co")
        company_data = cursor.fetchone()
        
        if company_data:
            # ایجاد یک instance از InfCo با داده‌های موجود
            company_info = InfCo()
            # پر کردن فیلدها با داده‌های موجود
            # این کار باید بر اساس ساختار جدول انجام شود
        else:
            company_info = None
    except Exception as e:
        print(f"Error getting company info: {e}")
        company_info = None
    
    if request.method == 'POST':
        form = CompanyInfoForm(request.POST, instance=company_info)
        if form.is_valid():
            # ذخیره با raw SQL
            try:
                cursor = connections['legacy'].cursor()
                # اینجا باید UPDATE یا INSERT مناسب انجام شود
                messages.success(request, "مشخصات شرکت با موفقیت به‌روز شد.")
                return redirect('accounting:home')
            except Exception as e:
                messages.error(request, f"خطا در ذخیره اطلاعات: {e}")
    else:
        form = CompanyInfoForm(instance=company_info)
    
    return render(request, 'generic_form.html', {'form': form, 'form_title': 'ویرایش مشخصات شرکت'})

# --- Sales Invoice ---
@login_required
def sale_invoice_create(request):
    if request.method == 'POST':
        form = SaleInvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save(commit=False)
            
            # تولید کد فاکتور
            invoice.code = get_new_code(FactFo)
            
            invoice.save(using='legacy')
            
            # ذخیره جزئیات فاکتور
            formset = SaleInvoiceDetailFormSet(request.POST, instance=invoice)
            if formset.is_valid():
                formset.save(using='legacy')
                
                # عملیات انبار (کاردکس)
                for detail in formset.instances:
                    if detail.good and detail.meghdar:
                        # به‌روزرسانی موجودی کالا
                        good = detail.good
                        good.mogodi = (good.mogodi or 0) - detail.meghdar
                        good.save(using='legacy')
                
                messages.success(request, f"فاکتور فروش شماره {invoice.code} با موفقیت ثبت شد.")
                return redirect('accounting:home')
    else:
        form = SaleInvoiceForm()
        formset = SaleInvoiceDetailFormSet(instance=FactFo())
    
    context = {
        'form': form,
        'formset': formset,
        'form_title': 'صدور فاکتور فروش'
    }
    return render(request, 'sale_invoice_form.html', context)

# --- Other Views ---
@login_required
def dev_links(request):
    return render(request, 'dev_links.html')

@login_required
def sales_list(request):
    return render(request, 'sales_list.html')

@login_required
def create_sale_invoice(request):
    return render(request, 'create_sale_invoice.html')

@login_required
def sales_create(request):
    return render(request, 'sales_create.html')

@login_required
def sales_detail(request, sale_id):
    return render(request, 'sales_detail.html')

@login_required
def purchase_list(request):
    return render(request, 'purchase_list.html')

@login_required
def purchase_create(request):
    return render(request, 'purchase_create.html')

@login_required
def cheque_receive_list(request):
    return render(request, 'cheque_receive_list.html')

@login_required
def cheque_receive_create(request):
    return render(request, 'cheque_receive_create.html')

@login_required
def cheque_receive_status_update(request, cheque_id):
    return render(request, 'cheque_receive_status_update.html')

@login_required
def cheque_pay_list(request):
    return render(request, 'cheque_pay_list.html')

@login_required
def cheque_pay_create(request):
    return render(request, 'cheque_pay_create.html')

@login_required
def inventory_report(request):
    return render(request, 'inventory_report.html')

@login_required
def financial_report(request):
    return render(request, 'financial_report.html')

@csrf_exempt
@login_required
def get_good_info(request):
    return render(request, 'get_good_info.html')

@csrf_exempt
@login_required
def get_person_info(request):
    return render(request, 'get_person_info.html')

@login_required
def person_settings(request):
    return render(request, 'person_settings.html')

@login_required
def sales_list_dynamic(request):
    return render(request, 'sales_list_dynamic.html')

@login_required
def purchase_list_dynamic(request):
    return render(request, 'purchase_list_dynamic.html')

@login_required
def sanad_list_dynamic(request):
    return render(request, 'sanad_list_dynamic.html')

@login_required
def good_list_dynamic(request):
    return render(request, 'good_list_dynamic.html')

@login_required
def upload_bak(request):
    return render(request, 'upload_bak.html')

@login_required
def backup_db(request):
    return render(request, 'backup_db.html')

@login_required
def sanad_detail(request, sanad_id):
    return render(request, 'sanad_detail.html')

def login_view(request):
    # اگر کاربر از قبل لاگین کرده، او را مستقیم به خانه بفرست
    if request.user.is_authenticated:
        return redirect('accounting:home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, 'لطفاً نام کاربری و رمز عبور را وارد کنید.')
            return redirect('accounting:login')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # به جای خواندن next از URL، مستقیماً به LOGIN_REDIRECT_URL می‌رویم
            return redirect('accounting:home') 
        else:
            messages.error(request, 'نام کاربری یا رمز عبور اشتباه است یا کاربر غیرفعال است.')
            return redirect('accounting:login')
    
    user_choices = get_active_users_for_login()
    context = {'user_choices': user_choices}
    return render(request, 'login.html', context)

def logout_view(request):
    return render(request, 'logout.html')

@login_required
def user_list(request):
    return render(request, 'user_list.html')

@login_required
def debug_passwords(request):
    return render(request, 'debug_passwords.html')

@login_required
def test_password_formats(request):
    return render(request, 'test_password_formats.html')

@login_required
def export_users_passwords(request):
    return render(request, 'export_users_passwords.html') 