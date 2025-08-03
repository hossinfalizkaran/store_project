# accounting/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Max, Q
from django.core.paginator import Paginator
from django.db import connections, transaction
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from decimal import Decimal
import json
from datetime import datetime
import jdatetime
import pytz

# 1. ایمپورت کردن تمام مدل‌های مورد نیاز
from .models import (
    Perinf, Pergrp, Goodinf, Goodgrps, Sanad, Stores, SandoghTbl,
    Bank, Ldaramad, LHazine, InfCo, Fiscalyear, Checkband, 
    FactFo, FactFoDetail, Kardex, Kharid, ChequesRecieve, ChequePay,
    Chequerecievelog, ChequepayLog, GetRecieve, Settings, Users
)

# 2. ایمپورت کردن تمام فرم‌های مورد نیاز
from .forms import (
    PersonForm, GoodForm, StoreForm, SandoghForm, BankForm,
    IncomeForm, ExpenseForm, CompanyInfoForm, FiscalYearForm, CheckBandForm,
    SaleInvoiceForm, SaleInvoiceDetailFormSet
)

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
    لیستی از نام‌های کاربری فعال و دارای رمز عبور را برای نمایش در dropdown لاگین برمی‌گرداند.
    """
    try:
        cursor = connections['legacy'].cursor()
        cursor.execute("""
            SELECT Name FROM Users 
            WHERE Is_Active = 1 
            AND Pass IS NOT NULL 
            AND Pass != '' 
            AND Name != 'مدير'
            ORDER BY Name
        """)
        users = cursor.fetchall()
        return [user[0] for user in users]
    except Exception as e:
        print(f"Error getting active users: {e}")
        return []

def get_new_code(model):
    """یک کد جدید بر اساس بزرگترین کد موجود در مدل ایجاد می‌کند."""
    max_code_result = model.objects.using('legacy').aggregate(max_code=Max('code'))
    max_code = max_code_result.get('max_code') or 0
    return max_code + 1

# یک تابع کمکی برای جلوگیری از تکرار کد
def generic_list_view(request, model, template_name, context_data):
    queryset = model.objects.using('legacy').all()
    
    # مرتب‌سازی پیش‌فرض (اگر مدل فیلد code داشت)
    if hasattr(model, 'code'):
        queryset = queryset.order_by('code')
    elif hasattr(model, 'id'):
        queryset = queryset.order_by('id')

    # جستجو (مثال ساده)
    search_query = request.GET.get('q', '')
    if search_query and hasattr(model, 'name'):
        queryset = queryset.filter(name__icontains=search_query)

    paginator = Paginator(queryset, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    final_context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'total_count': paginator.count,
    }
    final_context.update(context_data)
    return render(request, template_name, final_context)

@login_required
def home(request):
    return render(request, 'home.html')

# --- بخش اشخاص ---
@login_required
def person_list(request):
    # این ویو منطق خاص خود را دارد
    persons_qs = Perinf.objects.using('legacy').select_related('grpcode').order_by('code')
    search_query = request.GET.get('q', '').strip()
    if search_query:
        persons_qs = persons_qs.filter(
            Q(fullname__icontains=search_query) | Q(code__icontains=search_query)
        )
    paginator = Paginator(persons_qs, 25)
    page_obj = paginator.get_page(request.GET.get('page'))
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'total_count': paginator.count,
    }
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

# --- بخش کالاها ---
@login_required
def good_list(request):
    # این ویو هم منطق خاص خود را دارد
    good_groups = Goodgrps.objects.using('legacy').all().order_by('code')
    goods_qs = Goodinf.objects.using('legacy').select_related('grpcode', 'unit').order_by('code')
    selected_group_id = request.GET.get('group', '')
    if selected_group_id and selected_group_id.isdigit():
        goods_qs = goods_qs.filter(grpcode_id=selected_group_id)
    search_query = request.GET.get('q', '').strip()
    if search_query:
        goods_qs = goods_qs.filter(Q(name__icontains=search_query) | Q(code__icontains=search_query))
    
    paginator = Paginator(goods_qs, 25)
    page_obj = paginator.get_page(request.GET.get('page'))
    
    context = {
        'page_obj': page_obj,
        'good_groups': good_groups,
        'selected_group_id': selected_group_id,
        'search_query': search_query,
        'total_count': paginator.count,
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

# --- بخش اسناد ---
@login_required
def sanad_list(request):
    # اتصال صریح به دیتابیس legacy
    sanads = Sanad.objects.using('legacy').all().order_by('-code')
    paginator = Paginator(sanads, 25)
    page_obj = paginator.get_page(request.GET.get('page'))
    context = {'page_obj': page_obj, 'title': 'لیست اسناد حسابداری'}
    return render(request, 'sanad_list.html', context)

# --- ویوهای اطلاعات پایه با استفاده از تابع کمکی ---
@login_required
def store_list(request):
    context = {
        'title': 'لیست انبارها',
        'headers': ['کد', 'نام انبار', 'توضیحات'],
        'fields_to_display': ['code', 'name', 'comment'],
        'create_url_name': 'accounting:store_create',
        'update_url_name': 'accounting:store_update',
        'delete_url_name': 'accounting:store_delete',
    }
    return generic_list_view(request, Stores, 'generic_list.html', context)

@login_required
def store_create(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            store = form.save(commit=False)
            store.code = get_new_code(Stores)
            store.save(using='legacy')
            messages.success(request, "انبار با موفقیت ایجاد شد.")
            return redirect('accounting:store_list')
    else:
        form = StoreForm()
    
    return render(request, 'generic_form.html', {'form': form, 'form_title': 'ایجاد انبار جدید'})

@login_required
def store_update(request, pk):
    store = get_object_or_404(Stores.objects.using('legacy'), pk=pk)
    if request.method == 'POST':
        form = StoreForm(request.POST, instance=store)
        if form.is_valid():
            form.save(using='legacy')
            messages.success(request, "انبار با موفقیت ویرایش شد.")
            return redirect('accounting:store_list')
    else:
        form = StoreForm(instance=store)
    
    return render(request, 'generic_form.html', {'form': form, 'form_title': 'ویرایش انبار'})

@login_required
def store_delete(request, pk):
    store = get_object_or_404(Stores.objects.using('legacy'), pk=pk)
    store.delete()
    messages.success(request, "انبار با موفقیت حذف شد.")
    return redirect('accounting:store_list')

@login_required
def sandogh_list(request):
    context = {
        'title': 'لیست صندوق‌ها',
        'headers': ['کد', 'نام صندوق', 'توضیحات'],
        'fields_to_display': ['code', 'name', 'comment'],
        'create_url_name': 'accounting:sandogh_create',
        'update_url_name': 'accounting:sandogh_update',
        'delete_url_name': 'accounting:sandogh_delete',
    }
    return generic_list_view(request, SandoghTbl, 'generic_list.html', context)

@login_required
def sandogh_create(request):
    if request.method == 'POST':
        form = SandoghForm(request.POST)
        if form.is_valid():
            sandogh = form.save(commit=False)
            sandogh.code = get_new_code(SandoghTbl)
            sandogh.save(using='legacy')
            messages.success(request, "صندوق با موفقیت ایجاد شد.")
            return redirect('accounting:sandogh_list')
    else:
        form = SandoghForm()
    
    return render(request, 'generic_form.html', {'form': form, 'form_title': 'ایجاد صندوق جدید'})

@login_required
def sandogh_update(request, pk):
    sandogh = get_object_or_404(SandoghTbl.objects.using('legacy'), pk=pk)
    if request.method == 'POST':
        form = SandoghForm(request.POST, instance=sandogh)
        if form.is_valid():
            form.save(using='legacy')
            messages.success(request, "صندوق با موفقیت ویرایش شد.")
            return redirect('accounting:sandogh_list')
    else:
        form = SandoghForm(instance=sandogh)
    
    return render(request, 'generic_form.html', {'form': form, 'form_title': 'ویرایش صندوق'})

@login_required
def sandogh_delete(request, pk):
    sandogh = get_object_or_404(SandoghTbl.objects.using('legacy'), pk=pk)
    sandogh.delete()
    messages.success(request, "صندوق با موفقیت حذف شد.")
    return redirect('accounting:sandogh_list')

@login_required
def bank_list(request):
    context = {
        'title': 'لیست بانک‌ها',
        'headers': ['کد', 'نام بانک', 'شعبه', 'شماره حساب'],
        'fields_to_display': ['code', 'name', 'shobe', 'sh_h'],
        'create_url_name': 'accounting:bank_create',
        'update_url_name': 'accounting:bank_update',
        'delete_url_name': 'accounting:bank_delete',
    }
    return generic_list_view(request, Bank, 'generic_list.html', context)

@login_required
def bank_create(request):
    if request.method == 'POST':
        form = BankForm(request.POST)
        if form.is_valid():
            bank = form.save(commit=False)
            bank.code = get_new_code(Bank)
            bank.save(using='legacy')
            messages.success(request, "بانک با موفقیت ایجاد شد.")
            return redirect('accounting:bank_list')
    else:
        form = BankForm()
    
    return render(request, 'generic_form.html', {'form': form, 'form_title': 'ایجاد بانک جدید'})

@login_required
def bank_update(request, pk):
    bank = get_object_or_404(Bank.objects.using('legacy'), pk=pk)
    if request.method == 'POST':
        form = BankForm(request.POST, instance=bank)
        if form.is_valid():
            form.save(using='legacy')
            messages.success(request, "بانک با موفقیت ویرایش شد.")
            return redirect('accounting:bank_list')
    else:
        form = BankForm(instance=bank)
    
    return render(request, 'generic_form.html', {'form': form, 'form_title': 'ویرایش بانک'})

@login_required
def bank_delete(request, pk):
    bank = get_object_or_404(Bank.objects.using('legacy'), pk=pk)
    bank.delete()
    messages.success(request, "بانک با موفقیت حذف شد.")
    return redirect('accounting:bank_list')

@login_required
def income_list(request):
    context = {
        'title': 'لیست درآمدها',
        'headers': ['کد', 'نام درآمد', 'توضیحات'],
        'fields_to_display': ['code', 'name', 'comment'],
        'create_url_name': 'accounting:income_create',
        'update_url_name': 'accounting:income_update',
        'delete_url_name': 'accounting:income_delete',
    }
    return generic_list_view(request, Ldaramad, 'generic_list.html', context)

@login_required
def income_create(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.code = get_new_code(Ldaramad)
            income.save(using='legacy')
            messages.success(request, "درآمد با موفقیت ایجاد شد.")
            return redirect('accounting:income_list')
    else:
        form = IncomeForm()
    
    return render(request, 'generic_form.html', {'form': form, 'form_title': 'ایجاد درآمد جدید'})

@login_required
def income_update(request, pk):
    income = get_object_or_404(Ldaramad.objects.using('legacy'), pk=pk)
    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save(using='legacy')
            messages.success(request, "درآمد با موفقیت ویرایش شد.")
            return redirect('accounting:income_list')
    else:
        form = IncomeForm(instance=income)
    
    return render(request, 'generic_form.html', {'form': form, 'form_title': 'ویرایش درآمد'})

@login_required
def income_delete(request, pk):
    income = get_object_or_404(Ldaramad.objects.using('legacy'), pk=pk)
    income.delete()
    messages.success(request, "درآمد با موفقیت حذف شد.")
    return redirect('accounting:income_list')

@login_required
def expense_list(request):
    context = {
        'title': 'لیست هزینه‌ها',
        'headers': ['کد', 'نام هزینه', 'توضیحات'],
        'fields_to_display': ['code', 'name', 'comment'],
        'create_url_name': 'accounting:expense_create',
        'update_url_name': 'accounting:expense_update',
        'delete_url_name': 'accounting:expense_delete',
    }
    return generic_list_view(request, LHazine, 'generic_list.html', context)

@login_required
def expense_create(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.code = get_new_code(LHazine)
            expense.save(using='legacy')
            messages.success(request, "هزینه با موفقیت ایجاد شد.")
            return redirect('accounting:expense_list')
    else:
        form = ExpenseForm()
    
    return render(request, 'generic_form.html', {'form': form, 'form_title': 'ایجاد هزینه جدید'})

@login_required
def expense_update(request, pk):
    expense = get_object_or_404(LHazine.objects.using('legacy'), pk=pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save(using='legacy')
            messages.success(request, "هزینه با موفقیت ویرایش شد.")
            return redirect('accounting:expense_list')
    else:
        form = ExpenseForm(instance=expense)
    
    return render(request, 'generic_form.html', {'form': form, 'form_title': 'ویرایش هزینه'})

@login_required
def expense_delete(request, pk):
    expense = get_object_or_404(LHazine.objects.using('legacy'), pk=pk)
    expense.delete()
    messages.success(request, "هزینه با موفقیت حذف شد.")
    return redirect('accounting:expense_list')

@login_required
def fiscal_year_list(request):
    context = {
        'title': 'لیست دوره‌های مالی',
        'headers': ['کد', 'نام دوره', 'تاریخ شروع', 'تاریخ پایان'],
        'fields_to_display': ['code', 'name', 'startdate', 'enddate'],
        'create_url_name': 'accounting:fiscal_year_create',
        'update_url_name': 'accounting:fiscal_year_update',
        'delete_url_name': 'accounting:fiscal_year_delete',
    }
    return generic_list_view(request, Fiscalyear, 'generic_list.html', context)

@login_required
def fiscal_year_create(request):
    if request.method == 'POST':
        form = FiscalYearForm(request.POST)
        if form.is_valid():
            fiscal_year = form.save(commit=False)
            fiscal_year.code = get_new_code(Fiscalyear)
            fiscal_year.save(using='legacy')
            messages.success(request, "دوره مالی با موفقیت ایجاد شد.")
            return redirect('accounting:fiscal_year_list')
    else:
        form = FiscalYearForm()
    
    return render(request, 'generic_form.html', {'form': form, 'form_title': 'ایجاد دوره مالی جدید'})

@login_required
def fiscal_year_update(request, pk):
    fiscal_year = get_object_or_404(Fiscalyear.objects.using('legacy'), pk=pk)
    if request.method == 'POST':
        form = FiscalYearForm(request.POST, instance=fiscal_year)
        if form.is_valid():
            form.save(using='legacy')
            messages.success(request, "دوره مالی با موفقیت ویرایش شد.")
            return redirect('accounting:fiscal_year_list')
    else:
        form = FiscalYearForm(instance=fiscal_year)
    
    return render(request, 'generic_form.html', {'form': form, 'form_title': 'ویرایش دوره مالی'})

@login_required
def fiscal_year_delete(request, pk):
    fiscal_year = get_object_or_404(Fiscalyear.objects.using('legacy'), pk=pk)
    fiscal_year.delete()
    messages.success(request, "دوره مالی با موفقیت حذف شد.")
    return redirect('accounting:fiscal_year_list')

@login_required
def check_band_list(request):
    context = {
        'title': 'لیست دسته چک‌ها',
        'headers': ['کد', 'نام دسته', 'شماره شروع', 'شماره پایان'],
        'fields_to_display': ['code', 'name', 'startno', 'endno'],
        'create_url_name': 'accounting:check_band_create',
        'update_url_name': 'accounting:check_band_update',
        'delete_url_name': 'accounting:check_band_delete',
    }
    return generic_list_view(request, Checkband, 'generic_list.html', context)

@login_required
def check_band_create(request):
    if request.method == 'POST':
        form = CheckBandForm(request.POST)
        if form.is_valid():
            check_band = form.save(commit=False)
            check_band.code = get_new_code(Checkband)
            check_band.save(using='legacy')
            messages.success(request, "دسته چک با موفقیت ایجاد شد.")
            return redirect('accounting:check_band_list')
    else:
        form = CheckBandForm()
    
    return render(request, 'generic_form.html', {'form': form, 'form_title': 'ایجاد دسته چک جدید'})

@login_required
def check_band_update(request, pk):
    check_band = get_object_or_404(Checkband.objects.using('legacy'), pk=pk)
    if request.method == 'POST':
        form = CheckBandForm(request.POST, instance=check_band)
        if form.is_valid():
            form.save(using='legacy')
            messages.success(request, "دسته چک با موفقیت ویرایش شد.")
            return redirect('accounting:check_band_list')
    else:
        form = CheckBandForm(instance=check_band)
    
    return render(request, 'generic_form.html', {'form': form, 'form_title': 'ویرایش دسته چک'})

@login_required
def check_band_delete(request, pk):
    check_band = get_object_or_404(Checkband.objects.using('legacy'), pk=pk)
    check_band.delete()
    messages.success(request, "دسته چک با موفقیت حذف شد.")
    return redirect('accounting:check_band_list')

# ویو ویرایش مشخصات شرکت - اصلاح شده برای مدل InfCo
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

# --- بخش فاکتور فروش ---
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

# --- سایر ویوهای موجود ---
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
    return render(request, 'login.html')

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