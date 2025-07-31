import os
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.http import FileResponse
import subprocess
import zipfile
import jdatetime
import pytz
from datetime import datetime
from .models import Sanad, SanadDetail, Perinf, Pergrp
from django.core.paginator import Paginator
from django.db import models
import shutil
import re
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Settings
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Users
import hashlib
from django.db import connections
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.utils import timezone
from decimal import Decimal
import json
from datetime import datetime

from .models import (
    Perinf, Goodinf, Sanad, SanadDetail, Kardex,
    FactFo, FactFoDetail, Kharid, ChequesRecieve, ChequePay,
    Chequerecievelog, ChequepayLog, GetRecieve, Stores
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


# ========================================
# VIEW صفحه اصلی
# ========================================

@login_required
def home(request):
    """
    صفحه اصلی سیستم
    """
    user_id = request.user.id
    
    # دریافت آمار کلی
    total_customers = Perinf.objects.filter(status=1).count()
    total_goods = Goodinf.objects.filter(status=1).count()
    total_sales = FactFo.objects.filter(status=1).count()  # حذف tmp=0 چون فیلد tmp وجود ندارد
    total_purchases = Kharid.objects.filter(status=1).count()  # حذف tmp=0 چون فیلد tmp وجود ندارد
    
    # تنظیمات پیش‌فرض (موقتاً)
    person_settings = {
        'sort_key': 'code',
        'visible_columns': ['code', 'name', 'tel1', 'status'],
        'show_inactive': False,
        'page_size': 20
    }
    sales_settings = {
        'sort_key': 'tarikh',
        'visible_columns': ['code', 'shakhs_code', 'tarikh', 'mablagh_factor'],
        'show_inactive': False,
        'page_size': 20
    }
    purchase_settings = {
        'sort_key': 'tarikh',
        'visible_columns': ['code', 'shakhs_code', 'tarikh', 'mablagh_factor'],
        'show_inactive': False,
        'page_size': 20
    }
    
    context = {
        'title': 'صفحه اصلی - سیستم حسابداری محک',
        'total_customers': total_customers,
        'total_goods': total_goods,
        'total_sales': total_sales,
        'total_purchases': total_purchases,
        'current_date': timezone.now(),
        'person_settings': person_settings,
        'sales_settings': sales_settings,
        'purchase_settings': purchase_settings,
    }
    
    return render(request, 'home.html', context)


@login_required
def dev_links(request):
    """
    صفحه لینک‌های توسعه برای تست سریع
    """
    context = {
        'title': 'لینک‌های توسعه - سیستم حسابداری محک',
    }
    return render(request, 'dev_links.html', context)


# ========================================
# VIEW های اصلی فروش
# ========================================

@login_required
def sales_list(request):
    """لیست فاکتورهای فروش"""
    sales = FactFo.objects.filter(status=1).order_by('-tarikh')  # حذف tmp=0 و type=1، استفاده از status=1 و tarikh
    context = {
        'sales': sales,
        'title': 'لیست فاکتورهای فروش'
    }
    return render(request, 'accounting/sales/list.html', context)


@login_required
def create_sale_invoice(request):
    """
    ایجاد فاکتور فروش جدید
    این View بر اساس فلوچارت عملیات فروش پیاده‌سازی شده است
    """
    if request.method == 'POST':
        try:
            with transaction.atomic():
                # دریافت داده‌های JSON از درخواست
                data = json.loads(request.body)
                
                # ========================================
                # مرحله ۱: اعتبارسنجی داده‌ها
                # ========================================
                
                # بررسی وجود مشتری
                customer_code = data.get('customer_code')
                if not customer_code:
                    return JsonResponse({
                        'success': False,
                        'message': 'کد مشتری الزامی است'
                    })
                
                try:
                    customer = Perinf.objects.get(code=customer_code)
                except Perinf.DoesNotExist:
                    return JsonResponse({
                        'success': False,
                        'message': 'مشتری یافت نشد'
                    })
                
                # بررسی آیتم‌های فاکتور
                items = data.get('items', [])
                if not items:
                    return JsonResponse({
                        'success': False,
                        'message': 'حداقل یک آیتم باید در فاکتور وجود داشته باشد'
                    })
                
                # بررسی موجودی کالاها
                for item in items:
                    good_code = item.get('good_code')
                    quantity = Decimal(item.get('quantity', 0))
                    store_code = item.get('store_code', 1)  # پیش‌فرض انبار اصلی
                    
                    try:
                        good = Goodinf.objects.get(code=good_code)
                        # بررسی موجودی در انبار
                        if good.mogodi and good.mogodi < quantity:
                            return JsonResponse({
                                'success': False,
                                'message': f'موجودی کالای {good.name} کافی نیست. موجودی: {good.mogodi}'
                            })
                    except Goodinf.DoesNotExist:
                        return JsonResponse({
                            'success': False,
                            'message': f'کالای با کد {good_code} یافت نشد'
                        })
                
                # ========================================
                # مرحله ۲: ایجاد فاکتور فروش
                # ========================================
                
                # تولید شماره فاکتور جدید
                last_fact = FactFo.objects.filter(type=1).order_by('-code').first()
                new_fact_code = (last_fact.code + 1) if last_fact else 1
                
                # محاسبه مبالغ
                total_amount = Decimal('0')
                total_tax = Decimal('0')
                total_charge = Decimal('0')
                
                for item in items:
                    quantity = Decimal(item.get('quantity', 0))
                    unit_price = Decimal(item.get('unit_price', 0))
                    item_total = quantity * unit_price
                    total_amount += item_total
                    
                    # محاسبه مالیات و عوارض
                    tax_percent = Decimal(item.get('tax_percent', 0))
                    charge_percent = Decimal(item.get('charge_percent', 0))
                    
                    item_tax = (item_total * tax_percent) / 100
                    item_charge = (item_total * charge_percent) / 100
                    
                    total_tax += item_tax
                    total_charge += item_charge
                
                # ایجاد فاکتور فروش
                sale_invoice = FactFo.objects.create(
                    code=new_fact_code,
                    shakhs_code=customer,
                    tarikh=data.get('date', timezone.now().strftime('%Y/%m/%d')),
                    mablagh_factor=total_amount + total_tax + total_charge,
                    tax=total_tax,
                    charge=total_charge,
                    sharh=data.get('description', ''),
                    status=1,  # فعال
                    com_index=request.user.id,
                    usercreated=request.user.id,
                    createdtime=timezone.now().strftime('%H:%M'),
                    createddate=timezone.now().strftime('%Y/%m/%d'),
                    owner=request.user.id
                )
                
                # ========================================
                # مرحله ۳: ایجاد ردیف‌های فاکتور
                # ========================================
                
                for index, item in enumerate(items, 1):
                    good_code = item.get('good_code')
                    quantity = Decimal(item.get('quantity', 0))
                    unit_price = Decimal(item.get('unit_price', 0))
                    store_code = item.get('store_code', 1)
                    
                    # ایجاد ردیف فاکتور
                    fact_detail = FactFoDetail.objects.create(
                        code=sale_invoice,
                        radif=index,
                        an_code=store_code,
                        kala_code=good_code,
                        meghdar=quantity,
                        naghdi=unit_price,
                        sharh=item.get('description', ''),
                        vaziyat=1,  # فعال
                        status=1,
                        com_index=request.user.id,
                        taxpercent=Decimal(item.get('tax_percent', 0)),
                        chargepercent=Decimal(item.get('charge_percent', 0)),
                        takhfif=Decimal(item.get('discount', 0))
                    )
                    
                    # ========================================
                    # مرحله ۴: عملیات انبار (ثبت در کاردکس)
                    # ========================================
                    
                    # ثبت خروجی در کاردکس
                    kardex = Kardex.objects.create(
                        date=sale_invoice.tarikh,
                        percode=customer_code,
                        anbar=store_code,
                        kala=good_code,
                        type=1,  # نوع عملیات فروش
                        code=str(new_fact_code),
                        tedad=-quantity,  # خروجی منفی
                        amount=unit_price,
                        status=1,
                        com_index=request.user.id,
                        sanad_code=None  # بعداً پر می‌شود
                    )
                    
                    # به‌روزرسانی موجودی کالا
                    good = Goodinf.objects.get(code=good_code)
                    if good.mogodi is not None:
                        good.mogodi -= quantity
                        good.sadere = (good.sadere or 0) + quantity
                        good.save()
                
                # ========================================
                # مرحله ۵: عملیات حسابداری (ایجاد سند)
                # ========================================
                
                # تولید شماره سند جدید
                last_sanad = Sanad.objects.order_by('-sanadid').first()
                new_sanad_id = (last_sanad.sanadid + 1) if last_sanad else 1
                
                # ایجاد سند حسابداری
                sanad = Sanad.objects.create(
                    sanadid=new_sanad_id,  # تغییر code به sanadid
                    tarikh=sale_invoice.tarikh,
                    sharh=f"سند فاکتور فروش شماره {new_fact_code}",
                    status=1,
                    com_index=request.user.id,
                    usercreated=str(request.user.id),
                    createdtime=timezone.now().strftime('%H:%M'),
                    createddate=timezone.now().strftime('%Y/%m/%d')
                )
                
                # ثبت آرتیکل‌های سند
                row_number = 1
                
                # آرتیکل ۱: بدهکاری مشتری
                SanadDetail.objects.create(
                    sanad=new_sanad_id,  # تغییر code به sanad
                    radif=row_number,
                    kol=1,  # حساب مشتریان
                    moin=customer_code,
                    sharh=f"بدهکاری مشتری - فاکتور {new_fact_code}",
                    bed=total_amount + total_tax + total_charge,
                    bes=0,
                    sanad_code=str(new_sanad_id),
                    sanad_type=1,  # نوع سند فروش
                    com_index=request.user.id,
                    usercreated=str(request.user.id),
                    createdtime=timezone.now().strftime('%H:%M'),
                    createddate=timezone.now().strftime('%Y/%m/%d')
                )
                row_number += 1
                
                # آرتیکل ۲: بستانکاری فروش
                SanadDetail.objects.create(
                    sanad=new_sanad_id,  # تغییر code به sanad
                    radif=row_number,
                    kol=4,  # حساب فروش
                    moin=1,  # حساب فروش
                    sharh=f"فروش کالا - فاکتور {new_fact_code}",
                    bed=0,
                    bes=total_amount,
                    sanad_code=str(new_sanad_id),
                    sanad_type=1,
                    com_index=request.user.id,
                    usercreated=str(request.user.id),
                    createdtime=timezone.now().strftime('%H:%M'),
                    createddate=timezone.now().strftime('%Y/%m/%d')
                )
                row_number += 1
                
                # آرتیکل ۳: بستانکاری مالیات (در صورت وجود)
                if total_tax > 0:
                    SanadDetail.objects.create(
                        sanad=new_sanad_id,  # تغییر code به sanad
                        radif=row_number,
                        kol=5,  # حساب مالیات
                        moin=1,  # حساب مالیات
                        sharh=f"مالیات بر ارزش افزوده - فاکتور {new_fact_code}",
                        bed=0,
                        bes=total_tax,
                        sanad_code=str(new_sanad_id),
                        sanad_type=1,
                        com_index=request.user.id,
                        usercreated=str(request.user.id),
                        createdtime=timezone.now().strftime('%H:%M'),
                        createddate=timezone.now().strftime('%Y/%m/%d')
                    )
                    row_number += 1
                
                # آرتیکل ۴: بستانکاری عوارض (در صورت وجود)
                if total_charge > 0:
                    SanadDetail.objects.create(
                        sanad=new_sanad_id,  # تغییر code به sanad
                        radif=row_number,
                        kol=6,  # حساب عوارض
                        moin=1,  # حساب عوارض
                        sharh=f"عوارض - فاکتور {new_fact_code}",
                        bed=0,
                        bes=total_charge,
                        sanad_code=str(new_sanad_id),
                        sanad_type=1,
                        com_index=request.user.id,
                        usercreated=str(request.user.id),
                        createdtime=timezone.now().strftime('%H:%M'),
                        createddate=timezone.now().strftime('%Y/%m/%d')
                    )
                    row_number += 1
                
                # به‌روزرسانی کد سند در فاکتور
                sale_invoice.sanad_code = new_sanad_id
                sale_invoice.save()
                
                # به‌روزرسانی کد سند در کاردکس
                Kardex.objects.filter(code=str(new_fact_code), type=1).update(
                    sanad_sanad=new_sanad_id  # تغییر code به sanad
                )
                
                # ========================================
                # مرحله ۶: عملیات خزانه‌داری (اختیاری)
                # ========================================
                
                # اگر پرداخت نقدی وجود دارد
                cash_payment = Decimal(data.get('cash_payment', 0))
                if cash_payment > 0:
                    # تولید شماره دریافت جدید
                    last_receive = GetRecieve.objects.filter(type=0).order_by('-code').first()
                    new_receive_code = (last_receive.code + 1) if last_receive else 1
                    
                    # ثبت دریافت نقدی
                    receive = GetRecieve.objects.create(
                        code=new_receive_code,
                        percode=customer_code,
                        amount=cash_payment,
                        date=sale_invoice.tarikh,
                        type=0,  # دریافت
                        status=1,
                        comment=f"پرداخت نقدی فاکتور {new_fact_code}",
                        usercreated=request.user.id,
                        createdtime=timezone.now().strftime('%H:%M'),
                        createddate=timezone.now().strftime('%Y/%m/%d'),
                        owner=request.user.id
                    )
                    
                    # ایجاد سند حسابداری برای دریافت
                    receive_sanad_id = new_sanad_id + 1
                    receive_sanad = Sanad.objects.create(
                        code=receive_sanad_id,
                        tarikh=sale_invoice.tarikh,
                        sharh=f"دریافت نقدی فاکتور {new_fact_code}",
                        status=1,
                        com_index=request.user.id,
                        usercreated=str(request.user.id),
                        createdtime=timezone.now().strftime('%H:%M'),
                        createddate=timezone.now().strftime('%Y/%m/%d')
                    )
                    
                    # آرتیکل‌های سند دریافت
                    SanadDetail.objects.create(
                        code=receive_sanad_id,
                        radif=1,
                        kol=3,  # حساب صندوق
                        moin=1,  # حساب صندوق
                        sharh=f"دریافت نقدی فاکتور {new_fact_code}",
                        bed=cash_payment,
                        bes=0,
                        sanad_code=str(receive_sanad_id),
                        sanad_type=3,  # نوع سند دریافت
                        com_index=request.user.id,
                        usercreated=str(request.user.id),
                        createdtime=timezone.now().strftime('%H:%M'),
                        createddate=timezone.now().strftime('%Y/%m/%d')
                    )
                    
                    SanadDetail.objects.create(
                        code=receive_sanad_id,
                        radif=2,
                        kol=1,  # حساب مشتریان
                        moin=customer_code,
                        sharh=f"بستانکاری مشتری - دریافت نقدی فاکتور {new_fact_code}",
                        bed=0,
                        bes=cash_payment,
                        sanad_code=str(receive_sanad_id),
                        sanad_type=3,
                        com_index=request.user.id,
                        usercreated=str(request.user.id),
                        createdtime=timezone.now().strftime('%H:%M'),
                        createddate=timezone.now().strftime('%Y/%m/%d')
                    )
                    
                    # به‌روزرسانی کد سند در دریافت
                    receive.vouchercode = receive_sanad_id
                    receive.save()
                
                return JsonResponse({
                    'success': True,
                    'message': 'فاکتور فروش با موفقیت ثبت شد',
                    'invoice_code': new_fact_code,
                    'sanad_id': new_sanad_id
                })
                
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'خطا در ثبت فاکتور: {str(e)}'
            })
    
    # نمایش فرم ایجاد فاکتور
    customers = Perinf.objects.filter(status=1)  # مشتریان فعال
    goods = Goodinf.objects.filter(status=1)  # کالاهای فعال
    stores = Stores.objects.all()
    
    context = {
        'customers': customers,
        'goods': goods,
        'stores': stores,
        'title': 'ایجاد فاکتور فروش جدید'
    }
    return render(request, 'accounting/sales/create_invoice.html', context)


@login_required
def sales_create(request):
    """ایجاد فاکتور فروش جدید"""
    if request.method == 'POST':
        try:
            with transaction.atomic():
                # دریافت داده‌های فاکتور
                data = json.loads(request.body)
                
                # ایجاد فاکتور فروش
                sale = FactFo.objects.create(
                    code=data['code'],
                    shakhs_code=data['customer_code'],
                    tarikh=data['date'],
                    sharh=data.get('description', ''),
                    status=1,
                    usercreated=request.user.id,
                    createdtime=timezone.now().strftime('%H:%M'),
                    createddate=timezone.now().strftime('%Y/%m/%d'),
                    owner=request.user.id
                )
                
                # پردازش آیتم‌های فاکتور
                for item in data['items']:
                    # ایجاد رکورد کاردکس (خروجی)
                    kardex = Kardex.objects.create(
                        code=sale.code,  # تغییر sanad به code
                        radif=item['row'],
                        type=1,  # خروجی
                        kala_code=item['good_code'],
                        meghdar=item['quantity'],
                        naghdi=item['unit_price'],
                        status=1,
                        com_index=request.user.id,
                        sanad_type=1,  # فروش
                        sharh=f"فروش - فاکتور {sale.code}"
                    )
                    
                    # ایجاد سند حسابداری
                    sanad = Sanad.objects.create(
                        sanadid=sale.code,  # تغییر code به sanadid
                        type=1,  # فروش
                        date=data['date'],
                        sharh=f"فروش کالا - فاکتور {sale.code}",
                        status=1,
                        usercreated=request.user.id,
                        createdtime=timezone.now().strftime('%H:%M'),
                        createddate=timezone.now().strftime('%Y/%m/%d'),
                        owner=request.user.id
                    )
                    
                    # ثبت بدهکاری مشتری
                    SanadDetail.objects.create(
                        sanad_code=sanad.code,
                        sanad_type=sanad.type,
                        radif=1,
                        kol=1,  # حساب مشتریان
                        moin=data['customer_code'],
                        sharh=f"بدهکاری مشتری - فاکتور {sale.code}",
                        bed=item['total_price'],
                        bes=0,
                        com_index=request.user.id
                    )
                    
                    # ثبت بستانکاری فروش
                    SanadDetail.objects.create(
                        sanad_code=sanad.code,
                        sanad_type=sanad.type,
                        radif=2,
                        kol=4,  # حساب فروش
                        moin=item['good_code'],
                        sharh=f"فروش کالا - فاکتور {sale.code}",
                        bed=0,
                        bes=item['total_price'],
                        com_index=request.user.id
                    )
                
                # اگر پرداخت نقدی وجود دارد
                if data.get('cash_payment', 0) > 0:
                    GetRecieve.objects.create(
                        sanadid=sale.code,  # تغییر code به sanadid
                        type=1,  # دریافت
                        percode=data['customer_code'],
                        date=data['date'],
                        cost=data['cash_payment'],
                        description=f"پرداخت نقدی فاکتور {sale.code}",
                        usercreated=request.user.id,
                        createdtime=timezone.now().strftime('%H:%M'),
                        createddate=timezone.now().strftime('%Y/%m/%d'),
                        owner=request.user.id
                    )
                
                return JsonResponse({
                    'success': True,
                    'message': 'فاکتور فروش با موفقیت ثبت شد',
                    'sale_id': sale.code
                })
                
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'خطا در ثبت فاکتور: {str(e)}'
            })
    
    # نمایش فرم ایجاد فاکتور
    customers = Perinf.objects.filter(type=1)  # مشتریان
    goods = Goodinf.objects.filter(active=True)
    
    context = {
        'customers': customers,
        'goods': goods,
        'title': 'ایجاد فاکتور فروش جدید'
    }
    return render(request, 'accounting/sales/create.html', context)


@login_required
def sales_detail(request, sale_id):
    """جزئیات فاکتور فروش"""
    sale = get_object_or_404(FactFo, code=sale_id, status=1)  # حذف type=1 و tmp=0
    kardex_items = Kardex.objects.filter(code=sale_id, type=1)
    sanad = Sanad.objects.filter(code=sale_id, type=1).first()
    
    context = {
        'sale': sale,
        'kardex_items': kardex_items,
        'sanad': sanad,
        'title': f'جزئیات فاکتور فروش {sale_id}'
    }
    return render(request, 'accounting/sales/detail.html', context)


# ========================================
# VIEW های اصلی خرید
# ========================================

@login_required
def purchase_list(request):
    """لیست فاکتورهای خرید"""
    purchases = Kharid.objects.filter(status=1).order_by('-tarikh')  # حذف tmp=0 و type=1، استفاده از status=1 و tarikh
    context = {
        'purchases': purchases,
        'title': 'لیست فاکتورهای خرید'
    }
    return render(request, 'accounting/purchase/list.html', context)


@login_required
def purchase_create(request):
    """ایجاد فاکتور خرید جدید"""
    if request.method == 'POST':
        try:
            with transaction.atomic():
                data = json.loads(request.body)
                
                # ایجاد فاکتور خرید
                purchase = Kharid.objects.create(
                    code=data['code'],
                    shakhs_code=data['supplier_code'],
                    tarikh=data['date'],  # تغییر date به tarikh
                    sharh=data.get('description', ''),
                    status=1,
                    usercreated=request.user.id,
                    createdtime=timezone.now().strftime('%H:%M'),
                    createddate=timezone.now().strftime('%Y/%m/%d'),
                    owner=request.user.id
                )
                
                # پردازش آیتم‌های خرید
                for item in data['items']:
                    # ایجاد رکورد کاردکس (ورودی)
                    kardex = Kardex.objects.create(
                        sanadid=purchase.code,  # تغییر code به sanadid
                        radif=item['row'],
                        type=0,  # ورودی
                        kala_code=item['good_code'],
                        meghdar=item['quantity'],
                        naghdi=item['unit_price'],
                        status=1,
                        com_index=request.user.id,
                        sanad_type=2,  # خرید
                        sharh=f"خرید - فاکتور {purchase.code}"
                    )
                    
                    # ایجاد سند حسابداری
                    sanad = Sanad.objects.create(
                        sanadid=purchase.code,  # تغییر code به sanadid
                        type=2,  # خرید
                        date=data['date'],
                        sharh=f"خرید کالا - فاکتور {purchase.code}",
                        status=1,
                        usercreated=request.user.id,
                        createdtime=timezone.now().strftime('%H:%M'),
                        createddate=timezone.now().strftime('%Y/%m/%d'),
                        owner=request.user.id
                    )
                    
                    # ثبت بدهکاری خرید
                    SanadDetail.objects.create(
                        sanad_code=sanad.code,
                        sanad_type=sanad.type,
                        radif=1,
                        kol=2,  # حساب خرید
                        moin=item['good_code'],
                        sharh=f"خرید کالا - فاکتور {purchase.code}",
                        bed=item['total_price'],
                        bes=0,
                        com_index=request.user.id
                    )
                    
                    # ثبت بستانکاری تامین‌کننده
                    SanadDetail.objects.create(
                        sanad_code=sanad.code,
                        sanad_type=sanad.type,
                        radif=2,
                        kol=1,  # حساب تامین‌کنندگان
                        moin=data['supplier_code'],
                        sharh=f"بستانکاری تامین‌کننده - فاکتور {purchase.code}",
                        bed=0,
                        bes=item['total_price'],
                        com_index=request.user.id
                    )
                
                return JsonResponse({
                    'success': True,
                    'message': 'فاکتور خرید با موفقیت ثبت شد',
                    'purchase_id': purchase.code
                })
                
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'خطا در ثبت فاکتور: {str(e)}'
            })
    
    # نمایش فرم ایجاد فاکتور
    suppliers = Perinf.objects.filter(type=2)  # تامین‌کنندگان
    goods = Goodinf.objects.filter(active=True)
    
    context = {
        'suppliers': suppliers,
        'goods': goods,
        'title': 'ایجاد فاکتور خرید جدید'
    }
    return render(request, 'accounting/purchase/create.html', context)


# ========================================
# VIEW های مدیریت چک
# ========================================

@login_required
def cheque_receive_list(request):
    """لیست چک‌های دریافتی"""
    cheques = ChequesRecieve.objects.filter(owner=request.user.id).order_by('-createddate')
    context = {
        'cheques': cheques,
        'title': 'لیست چک‌های دریافتی'
    }
    return render(request, 'accounting/cheque/receive_list.html', context)


@login_required
def cheque_receive_create(request):
    """ثبت چک دریافتی جدید"""
    if request.method == 'POST':
        try:
            with transaction.atomic():
                data = json.loads(request.body)
                
                # ثبت چک دریافتی
                cheque = ChequesRecieve.objects.create(
                    chequeid=data['cheque_id'],
                    chequedate=data['cheque_date'],
                    cost=Decimal(data['amount']),
                    bankname=data['bank_name'],
                    bankbranch=data.get('bank_branch', ''),
                    accountid=data.get('account_id', ''),
                    description=data.get('description', ''),
                    status=1,  # در انتظار وصول
                    percode=data['customer_code'],
                    usercreated=request.user.id,
                    createdtime=timezone.now().strftime('%H:%M'),
                    createddate=timezone.now().strftime('%Y/%m/%d'),
                    owner=request.user.id
                )
                
                # ثبت لاگ
                Chequerecievelog.objects.create(
                    chequerecieveid=cheque.id,
                    status=1,  # در انتظار وصول
                    entitycode=data['customer_code'],
                    date=timezone.now().strftime('%Y/%m/%d'),
                    location='ثبت اولیه',
                    usercreated=request.user.id,
                    createdtime=timezone.now().strftime('%H:%M'),
                    createddate=timezone.now().strftime('%Y/%m/%d'),
                    owner=request.user.id
                )
                
                return JsonResponse({
                    'success': True,
                    'message': 'چک دریافتی با موفقیت ثبت شد',
                    'cheque_id': cheque.id
                })
                
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'خطا در ثبت چک: {str(e)}'
            })
    
    customers = Perinf.objects.filter(type=1)  # مشتریان
    context = {
        'customers': customers,
        'title': 'ثبت چک دریافتی جدید'
    }
    return render(request, 'accounting/cheque/receive_create.html', context)


@login_required
def cheque_receive_status_update(request, cheque_id):
    """تغییر وضعیت چک دریافتی"""
    if request.method == 'POST':
        try:
            with transaction.atomic():
                data = json.loads(request.body)
                new_status = data['status']
                
                cheque = ChequesRecieve.objects.get(id=cheque_id)
                old_status = cheque.status
                cheque.status = new_status
                cheque.usermodified = request.user.id
                cheque.modifiedtime = timezone.now().strftime('%H:%M')
                cheque.modifieddate = timezone.now().strftime('%Y/%m/%d')
                cheque.save()
                
                # ثبت لاگ
                Chequerecievelog.objects.create(
                    chequerecieveid=cheque.id,
                    status=new_status,
                    entitycode=cheque.percode,
                    date=timezone.now().strftime('%Y/%m/%d'),
                    location=data.get('location', 'تغییر وضعیت'),
                    locationcomment=data.get('comment', ''),
                    usercreated=request.user.id,
                    createdtime=timezone.now().strftime('%H:%M'),
                    createddate=timezone.now().strftime('%Y/%m/%d'),
                    owner=request.user.id
                )
                
                # اگر چک وصول شد، سند حسابداری ایجاد کن
                if new_status == 2:  # وصول شده
                    sanad = Sanad.objects.create(
                        code=cheque.id,  # تغییر sanad به code
                        type=3,  # وصول چک
                        date=timezone.now().strftime('%Y/%m/%d'),
                        sharh=f"وصول چک {cheque.chequeid}",
                        status=1,
                        usercreated=request.user.id,
                        createdtime=timezone.now().strftime('%H:%M'),
                        createddate=timezone.now().strftime('%Y/%m/%d'),
                        owner=request.user.id
                    )
                    
                    # بدهکاری بانک
                    SanadDetail.objects.create(
                        sanad_code=sanad.code,
                        sanad_type=sanad.type,
                        radif=1,
                        kol=3,  # حساب بانک
                        moin=cheque.bankcode if hasattr(cheque, 'bankcode') else 1,
                        sharh=f"وصول چک {cheque.chequeid}",
                        bed=cheque.cost,
                        bes=0,
                        com_index=request.user.id
                    )
                    
                    # بستانکاری چک‌های دریافتی
                    SanadDetail.objects.create(
                        sanad_code=sanad.code,
                        sanad_type=sanad.type,
                        radif=2,
                        kol=5,  # حساب چک‌های دریافتی
                        moin=cheque.percode,
                        sharh=f"وصول چک {cheque.chequeid}",
                        bed=0,
                        bes=cheque.cost,
                        com_index=request.user.id
                    )
                
                return JsonResponse({
                    'success': True,
                    'message': 'وضعیت چک با موفقیت تغییر یافت'
                })
                
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'خطا در تغییر وضعیت: {str(e)}'
            })


@login_required
def cheque_pay_list(request):
    """لیست چک‌های پرداختی"""
    cheques = ChequePay.objects.filter(owner=request.user.id).order_by('-createddate')
    context = {
        'cheques': cheques,
        'title': 'لیست چک‌های پرداختی'
    }
    return render(request, 'accounting/cheque/pay_list.html', context)


@login_required
def cheque_pay_create(request):
    """ثبت چک پرداختی جدید"""
    if request.method == 'POST':
        try:
            with transaction.atomic():
                data = json.loads(request.body)
                
                # ثبت چک پرداختی
                cheque = ChequePay.objects.create(
                    chequeid=data['cheque_id'],
                    chequedate=data['cheque_date'],
                    cost=Decimal(data['amount']),
                    bankcode=data['bank_code'],
                    description=data.get('description', ''),
                    status=1,  # صادر شده
                    percode=data['supplier_code'],
                    usercreated=request.user.id,
                    createdtime=timezone.now().strftime('%H:%M'),
                    createddate=timezone.now().strftime('%Y/%m/%d'),
                    owner=request.user.id
                )
                
                # ثبت لاگ
                ChequepayLog.objects.create(
                    chequepayid=cheque.id,
                    status=1,  # صادر شده
                    entitycode=data['supplier_code'],
                    date=timezone.now().strftime('%Y/%m/%d'),
                    location='صدور چک',
                    usercreated=request.user.id,
                    createdtime=timezone.now().strftime('%H:%M'),
                    createddate=timezone.now().strftime('%Y/%m/%d'),
                    owner=request.user.id
                )
                
                # ایجاد سند حسابداری
                sanad = Sanad.objects.create(
                    code=cheque.id,  # تغییر sanad به code
                    type=4,  # صدور چک
                    date=timezone.now().strftime('%Y/%m/%d'),
                    sharh=f"صدور چک {cheque.chequeid}",
                    status=1,
                    usercreated=request.user.id,
                    createdtime=timezone.now().strftime('%H:%M'),
                    createddate=timezone.now().strftime('%Y/%m/%d'),
                    owner=request.user.id
                )
                
                # بدهکاری تامین‌کننده
                SanadDetail.objects.create(
                    sanad_code=sanad.code,
                    sanad_type=sanad.type,
                    radif=1,
                    kol=1,  # حساب تامین‌کنندگان
                    moin=data['supplier_code'],
                    sharh=f"بدهکاری تامین‌کننده - چک {cheque.chequeid}",
                    bed=cheque.cost,
                    bes=0,
                    com_index=request.user.id
                )
                
                # بستانکاری چک‌های پرداختی
                SanadDetail.objects.create(
                    sanad_code=sanad.code,
                    sanad_type=sanad.type,
                    radif=2,
                    kol=6,  # حساب چک‌های پرداختی
                    moin=cheque.bankcode,
                    sharh=f"صدور چک {cheque.chequeid}",
                    bed=0,
                    bes=cheque.cost,
                    com_index=request.user.id
                )
                
                return JsonResponse({
                    'success': True,
                    'message': 'چک پرداختی با موفقیت ثبت شد',
                    'cheque_id': cheque.id
                })
                
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'خطا در ثبت چک: {str(e)}'
            })
    
    suppliers = Perinf.objects.filter(type=2)  # تامین‌کنندگان
    banks = Bank.objects.all()
    context = {
        'suppliers': suppliers,
        'banks': banks,
        'title': 'ثبت چک پرداختی جدید'
    }
    return render(request, 'accounting/cheque/pay_create.html', context)


# ========================================
# VIEW های گزارش‌گیری
# ========================================

@login_required
def inventory_report(request):
    """گزارش موجودی انبار"""
    # اینجا می‌توانید کوئری‌های پیچیده برای گزارش موجودی بنویسید
    context = {
        'title': 'گزارش موجودی انبار'
    }
    return render(request, 'accounting/reports/inventory.html', context)


@login_required
def financial_report(request):
    """گزارش مالی"""
    context = {
        'title': 'گزارش مالی'
    }
    return render(request, 'accounting/reports/financial.html', context)


# ========================================
# API VIEW ها برای AJAX
# ========================================

@csrf_exempt
@login_required
def get_good_info(request):
    """دریافت اطلاعات کالا برای AJAX"""
    good_code = request.GET.get('good_code')
    try:
        good = Goodinf.objects.get(code=good_code)
        return JsonResponse({
            'success': True,
            'good': {
                'name': good.name,
                'price': float(good.price) if good.price else 0,
                'unit': good.unit
            }
        })
    except Goodinf.DoesNotExist:
        return JsonResponse({
            'success': False,
            'message': 'کالا یافت نشد'
        })


@csrf_exempt
@login_required
def get_person_info(request):
    """دریافت اطلاعات شخص برای AJAX"""
    person_code = request.GET.get('person_code')
    try:
        person = Perinf.objects.get(code=person_code)
        return JsonResponse({
            'success': True,
            'person': {
                'name': person.name,
                'tel': person.tel,
                'address': person.add1
            }
        })
    except Perinf.DoesNotExist:
        return JsonResponse({
            'success': False,
            'message': 'شخص یافت نشد'
        })


@login_required
def person_list(request):
    """
    نمایش لیست اشخاص با قابلیت جستجو و صفحه‌بندی (سازگار با SQLite و SQL Server).
    """
    from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
    from django.db.models import Q
    
    # queryset پایه
    persons_qs = Perinf.objects.using('legacy').select_related('grpcode').order_by('code')

    # منطق جستجو
    search_query = request.GET.get('q', '').strip()
    if search_query:
        # نرمال‌سازی ورودی کاربر
        normalized_query = normalize_persian_text(search_query)
        
        # استفاده از ORM جنگو برای ساخت کوئری
        # __icontains به صورت پیش‌فرض case-insensitive است
        persons_qs = persons_qs.filter(
            Q(fullname__icontains=normalized_query) |
            Q(code__icontains=normalized_query) |
            Q(tel1__icontains=normalized_query) |
            Q(mobile__icontains=normalized_query)
        )
        
        # برای حل مشکل "ی" و "ک" عربی، یک فیلتر اضافه می‌کنیم
        # این بخش کمی پیچیده‌تر است چون ORM مستقیم آن را پشتیبانی نمی‌کند
        # اما راه حل ساده‌تر این است که در جستجوی fullname، هر دو حالت را در نظر بگیریم
        arabic_query = normalized_query.replace('ی', 'ي').replace('ک', 'ك')
        if arabic_query != normalized_query:
             persons_qs = persons_qs | Perinf.objects.using('legacy').select_related('grpcode').filter(
                Q(fullname__icontains=arabic_query)
             )

    # منطق صفحه‌بندی (بدون تغییر)
    page_number = request.GET.get('page', 1)
    paginator = Paginator(persons_qs, 25)

    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'total_count': paginator.count,
        'title': 'لیست اشخاص',
    }
    return render(request, 'person_list.html', context)


@login_required
def person_detail(request, person_id):
    """
    نمایش جزئیات شخص
    """
    from django.shortcuts import get_object_or_404
    
    # دریافت شخص مورد نظر
    person = get_object_or_404(Perinf.objects.using('legacy').select_related('grpcode'), code=person_id)
    
    context = {
        'person': person,
        'title': f'جزئیات شخص - {person.fullname or person.code}',
    }
    
    return render(request, 'person_detail.html', context)


@login_required
def person_create(request):
    """
    ایجاد شخص جدید
    """
    from django.shortcuts import redirect
    from .forms import PersonForm
    
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            # استفاده از دیتابیس legacy
            person.save(using='legacy')
            messages.success(request, f'شخص "{person.fullname or person.name}" با موفقیت ایجاد شد.')
            return redirect('person_list')
    else:
        form = PersonForm()
    
    context = {
        'form': form,
        'title': 'ایجاد شخص جدید',
        'is_create': True,
    }
    
    return render(request, 'person_form.html', context)


@login_required
def person_update(request, person_id):
    """
    ویرایش شخص موجود
    """
    from django.shortcuts import redirect
    from .forms import PersonForm
    
    person = get_object_or_404(Perinf.objects.using('legacy'), code=person_id)
    
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            person = form.save(commit=False)
            # استفاده از دیتابیس legacy
            person.save(using='legacy')
            messages.success(request, f'اطلاعات شخص "{person.fullname or person.name}" با موفقیت بروزرسانی شد.')
            return redirect('person_detail', person_id=person.code)
    else:
        form = PersonForm(instance=person)
    
    context = {
        'form': form,
        'person': person,
        'title': f'ویرایش شخص - {person.fullname or person.name or person.code}',
        'is_create': False,
    }
    
    return render(request, 'person_form.html', context)


# ========================================
# View های مربوط به کالاها
# ========================================

@login_required
def good_list(request):
    """
    لیست کالاها با قابلیت جستجو و صفحه‌بندی
    """
    from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
    from django.db.models import Q
    
    # queryset پایه
    goods_qs = Goodinf.objects.using('legacy').select_related('grpcode', 'unit', 'unit2', 'store').order_by('code')

    # منطق جستجو
    search_query = request.GET.get('q', '').strip()
    if search_query:
        # نرمال‌سازی ورودی کاربر
        normalized_query = normalize_persian_text(search_query)
        
        # استفاده از ORM جنگو برای ساخت کوئری
        goods_qs = goods_qs.filter(
            Q(name__icontains=normalized_query) |
            Q(code__icontains=normalized_query) |
            Q(abbname__icontains=normalized_query) |
            Q(kala_name__icontains=normalized_query)
        )
        
        # برای حل مشکل "ی" و "ک" عربی، یک فیلتر اضافه می‌کنیم
        arabic_query = normalized_query.replace('ی', 'ي').replace('ک', 'ك')
        if arabic_query != normalized_query:
             goods_qs = goods_qs | Goodinf.objects.using('legacy').select_related('grpcode', 'unit', 'unit2', 'store').filter(
                Q(name__icontains=arabic_query)
             )

    # منطق صفحه‌بندی
    page_number = request.GET.get('page', 1)
    paginator = Paginator(goods_qs, 25)

    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'total_count': paginator.count,
        'title': 'لیست کالاها',
    }
    return render(request, 'good_list.html', context)


@login_required
def good_detail(request, good_id):
    """
    نمایش جزئیات کالا
    """
    from django.shortcuts import get_object_or_404
    
    # دریافت کالای مورد نظر
    good = get_object_or_404(Goodinf.objects.using('legacy').select_related('grpcode', 'unit', 'unit2', 'store'), code=good_id)
    
    context = {
        'good': good,
        'title': f'جزئیات کالا - {good.name or good.code}',
    }
    
    return render(request, 'good_detail.html', context)


@login_required
def good_create(request):
    """
    ایجاد کالای جدید
    """
    from django.shortcuts import redirect
    from .forms import GoodForm
    
    if request.method == 'POST':
        form = GoodForm(request.POST)
        if form.is_valid():
            good = form.save(commit=False)
            
            # تولید کد جدید اگر کد خالی باشد
            if not good.code:
                try:
                    max_code = Goodinf.objects.using('legacy').aggregate(
                        models.Max('code')
                    )['code__max'] or 0
                    good.code = max_code + 1
                except:
                    good.code = 1
            
            # استفاده از دیتابیس legacy
            good.save(using='legacy')
            messages.success(request, f'کالای "{good.name or good.code}" با موفقیت ایجاد شد.')
            return redirect('good_list')
    else:
        form = GoodForm()
    
    context = {
        'form': form,
        'title': 'ایجاد کالای جدید',
        'is_create': True,
    }
    
    return render(request, 'good_form.html', context)


@login_required
def good_update(request, good_id):
    """
    ویرایش کالای موجود
    """
    from django.shortcuts import redirect
    from .forms import GoodForm
    
    good = get_object_or_404(Goodinf.objects.using('legacy'), code=good_id)
    
    if request.method == 'POST':
        form = GoodForm(request.POST, instance=good)
        if form.is_valid():
            good = form.save(commit=False)
            # استفاده از دیتابیس legacy
            good.save(using='legacy')
            messages.success(request, f'اطلاعات کالای "{good.name or good.code}" با موفقیت بروزرسانی شد.')
            return redirect('good_detail', good_id=good.code)
    else:
        form = GoodForm(instance=good)
    
    context = {
        'form': form,
        'good': good,
        'title': f'ویرایش کالا - {good.name or good.code}',
        'is_create': False,
    }
    
    return render(request, 'good_form.html', context)


@login_required
def person_settings(request):
    """
    تنظیمات نمایش لیست اشخاص
    """
    from .utils import get_person_list_settings, save_user_list_settings
    
    user_id = request.user.id
    
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # ذخیره تنظیمات مرتب‌سازی
            if 'sort_key' in data:
                save_user_list_settings(user_id, 3, 1, 'sort', data['sort_key'])
            
            # ذخیره تنظیمات ستون‌های قابل نمایش
            if 'visible_columns' in data:
                columns_str = ','.join(data['visible_columns'])
                save_user_list_settings(user_id, 3, 2, 'columns', columns_str)
            
            # ذخیره تنظیمات boolean
            if 'show_inactive' in data:
                save_user_list_settings(user_id, 3, 3, 'boolean', data['show_inactive'])
            
            # ذخیره تنظیمات تعداد آیتم در صفحه
            if 'page_size' in data:
                save_user_list_settings(user_id, 3, 4, 'page_size', data['page_size'])
            
            return JsonResponse({
                'success': True,
                'message': 'تنظیمات با موفقیت ذخیره شد'
            })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'خطا در ذخیره تنظیمات: {str(e)}'
            })
    
    # دریافت تنظیمات فعلی
    settings_dict = get_person_list_settings(user_id)
    
    # لیست ستون‌های موجود
    available_columns = [
        {'code': 'code', 'name': 'کد'},
        {'code': 'name', 'name': 'نام'},
        {'code': 'lname', 'name': 'نام خانوادگی'},
        {'code': 'fullname', 'name': 'نام کامل'},
        {'code': 'tel1', 'name': 'تلفن'},
        {'code': 'mobile', 'name': 'موبایل'},
        {'code': 'credit', 'name': 'اعتبار'},
        {'code': 'status', 'name': 'وضعیت'},
        {'code': 'addr1', 'name': 'آدرس'},
        {'code': 'email', 'name': 'ایمیل'},
    ]
    
    # لیست گزینه‌های مرتب‌سازی
    sort_options = [
        {'code': 'code', 'name': 'کد'},
        {'code': 'name', 'name': 'نام'},
        {'code': 'lname', 'name': 'نام خانوادگی'},
        {'code': 'lname,name', 'name': 'نام خانوادگی و نام'},
        {'code': 'fullname', 'name': 'نام کامل'},
        {'code': 'credit', 'name': 'اعتبار'},
        {'code': 'status', 'name': 'وضعیت'},
    ]
    
    context = {
        'title': 'تنظیمات نمایش لیست اشخاص',
        'settings': settings_dict,
        'available_columns': available_columns,
        'sort_options': sort_options,
    }
    
    return render(request, 'accounting/person/settings.html', context)


@login_required
def sales_list_dynamic(request):
    """
    لیست فاکتورهای فروش با تنظیمات داینامیک
    """
    from .utils import get_sales_list_settings, get_list_context, get_column_display_name, get_column_value, format_column_value
    
    # دریافت تنظیمات لیست برای کاربر
    user_id = request.user.id
    settings_dict = get_sales_list_settings(user_id)
    
    # دریافت queryset اصلی
    queryset = FactFo.objects.filter(status=1)  # حذف type=1 و tmp=0
    
    # اعمال تنظیمات و دریافت context
    context = get_list_context(queryset, settings_dict, request)
    
    # اضافه کردن اطلاعات اضافی
    context.update({
        'title': 'لیست فاکتورهای فروش',
        'model_name': 'FactFo',
        'get_column_display_name': get_column_display_name,
        'get_column_value': get_column_value,
        'format_column_value': format_column_value,
    })
    
    return render(request, 'accounting/sales/list_dynamic.html', context)


@login_required
def purchase_list_dynamic(request):
    """
    لیست فاکتورهای خرید با تنظیمات داینامیک
    """
    from .utils import get_purchase_list_settings, get_list_context, get_column_display_name, get_column_value, format_column_value
    
    # دریافت تنظیمات لیست برای کاربر
    user_id = request.user.id
    settings_dict = get_purchase_list_settings(user_id)
    
    # دریافت queryset اصلی
    queryset = Kharid.objects.filter(status=1)  # حذف type=1 و tmp=0
    
    # اعمال تنظیمات و دریافت context
    context = get_list_context(queryset, settings_dict, request)
    
    # اضافه کردن اطلاعات اضافی
    context.update({
        'title': 'لیست فاکتورهای خرید',
        'model_name': 'Kharid',
        'get_column_display_name': get_column_display_name,
        'get_column_value': get_column_value,
        'format_column_value': format_column_value,
    })
    
    return render(request, 'accounting/purchase/list_dynamic.html', context)


@login_required
def sanad_list_dynamic(request):
    """
    لیست اسناد حسابداری با تنظیمات داینامیک
    """
    from .utils import get_sanad_list_settings, get_list_context, get_column_display_name, get_column_value, format_column_value
    
    # دریافت تنظیمات لیست برای کاربر
    user_id = request.user.id
    settings_dict = get_sanad_list_settings(user_id)
    
    # دریافت queryset اصلی
    queryset = Sanad.objects.all()
    
    # اعمال تنظیمات و دریافت context
    context = get_list_context(queryset, settings_dict, request)
    
    # اضافه کردن اطلاعات اضافی
    context.update({
        'title': 'لیست اسناد حسابداری',
        'model_name': 'Sanad',
        'get_column_display_name': get_column_display_name,
        'get_column_value': get_column_value,
        'format_column_value': format_column_value,
    })
    
    return render(request, 'accounting/sanad/list_dynamic.html', context)


@login_required
def good_list_dynamic(request):
    """
    لیست کالاها با تنظیمات داینامیک
    """
    from .utils import get_good_list_settings, get_list_context, get_column_display_name, get_column_value, format_column_value
    
    # دریافت تنظیمات لیست برای کاربر
    user_id = request.user.id
    settings_dict = get_good_list_settings(user_id)
    
    # دریافت queryset اصلی
    queryset = Goodinf.objects.all()
    
    # اعمال تنظیمات و دریافت context
    context = get_list_context(queryset, settings_dict, request)
    
    # اضافه کردن اطلاعات اضافی
    context.update({
        'title': 'لیست کالاها',
        'model_name': 'Goodinf',
        'get_column_display_name': get_column_display_name,
        'get_column_value': get_column_value,
        'format_column_value': format_column_value,
    })
    
    return render(request, 'accounting/good/list_dynamic.html', context)


# ========================================
# VIEW های مدیریت فایل و پشتیبان‌گیری
# ========================================

@login_required
def upload_bak(request):
    """آپلود فایل پشتیبان"""
    if request.method == 'POST':
        uploaded_file = request.FILES.get('bak_file')
        if uploaded_file:
            # پردازش فایل آپلود شده
            messages.success(request, 'فایل با موفقیت آپلود شد')
        else:
            messages.error(request, 'لطفاً فایلی انتخاب کنید')
    
    return render(request, 'accounting/upload_bak.html', {'title': 'آپلود فایل پشتیبان'})


@login_required
def backup_db(request):
    """ایجاد پشتیبان از دیتابیس"""
    try:
        # ایجاد پشتیبان از دیتابیس
        messages.success(request, 'پشتیبان با موفقیت ایجاد شد')
    except Exception as e:
        messages.error(request, f'خطا در ایجاد پشتیبان: {str(e)}')
    
    return render(request, 'accounting/backup_db.html', {'title': 'پشتیبان‌گیری'})


# ========================================
# VIEW های مدیریت اسناد
# ========================================

@login_required
def sanad_list(request):
    """لیست اسناد حسابداری"""
    from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
    from django.db import connection
    
    # دریافت پارامترهای جستجو و مرتب‌سازی
    search_query = request.GET.get('search', '').strip()
    sort = request.GET.get('sort', 'date')
    order = request.GET.get('order', 'desc')
    page_size = int(request.GET.get('page_size', 20))
    page_number = request.GET.get('page', 1)
    
    # تعیین مرتب‌سازی
    if sort == 'date':
        order_by = 'Tarikh'
    elif sort == 'number':
        order_by = 'Code'
    elif sort == 'type':
        order_by = 'Zamaem'
    else:
        order_by = 'Tarikh'
    
    order_by += ' DESC' if order == 'desc' else ' ASC'
    
    # ساخت کوئری با جستجو
    where_clause = ""
    params = []
    
    if search_query:
        # استفاده از COLLATE برای جستجوی غیرحساس به حروف فارسی و عربی
        collation = "COLLATE Persian_100_CI_AI"
        where_clause = f"""
            WHERE (
                ISNULL(Code, '') LIKE %s OR
                ISNULL(Sharh, '') {collation} LIKE %s {collation} OR 
                ISNULL(SanadID, '') LIKE %s OR
                ISNULL(Tarikh, '') LIKE %s OR
                ISNULL(Zamaem, '') {collation} LIKE %s {collation}
            )
        """
        search_param = f'%{search_query}%'
        params = [search_param, search_param, search_param, search_param, search_param]
    
    # اجرای کوئری
    with connection.cursor() as cursor:
        count_query = f"SELECT COUNT(*) FROM Sanad {where_clause}"
        cursor.execute(count_query, params)
        total_count = cursor.fetchone()[0]
    
    with connection.cursor() as cursor:
        data_query = f"""
            SELECT * FROM Sanad 
            {where_clause}
            ORDER BY {order_by}
            OFFSET {(int(page_number) - 1) * page_size} ROWS 
            FETCH NEXT {page_size} ROWS ONLY
        """
        cursor.execute(data_query, params)
        sanads_data = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
    
    # تبدیل نتایج به QuerySet
    sanad_codes = [row[columns.index('Code')] for row in sanads_data]
    sanads = Sanad.objects.filter(code__in=sanad_codes).order_by('-tarikh')
    
    # صفحه‌بندی
    paginator = Paginator(sanads, page_size)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    
    context = {
        'sanads': page_obj,
        'search_query': search_query,
        'sort': sort,
        'order': order,
        'page_size': page_size,
        'total_count': total_count,
        'title': 'لیست اسناد حسابداری'
    }
    return render(request, 'accounting/sanad_list.html', context)


@login_required
def sanad_detail(request, sanad_id):
    """جزئیات سند حسابداری"""
    sanad = get_object_or_404(Sanad, sanadid=sanad_id)
    
    # استفاده از values() برای جلوگیری از مشکل id
    sanad_details_data = SanadDetail.objects.filter(sanad=sanad_id).values(
        'sanad', 'radif', 'kol', 'moin', 'tafzili', 'sharh', 'status',
        'bed', 'bes', 'sanad_code', 'sanad_type', 'meghdar', 'com_index',
        'zamaem', 'store', 'tafsili2', 'voucherdate', 'operationdate',
        'syscomment', 'currcode', 'curramount', 'currrate', 'usercode',
        'createdtime', 'createddate', 'modifiedtime', 'modifieddate',
        'usercreated', 'usermodified'
    )
    
    # محاسبه مجموع بدهکار و بستانکار
    total_bed = sum(detail['bed'] or 0 for detail in sanad_details_data)
    total_bes = sum(detail['bes'] or 0 for detail in sanad_details_data)
    
    context = {
        'sanad': sanad,
        'sanad_details': sanad_details_data,
        'total_bed': total_bed,
        'total_bes': total_bes,
        'title': f'جزئیات سند {sanad_id}'
    }
    return render(request, 'accounting/sanad/detail.html', context)


# ========================================
# VIEW های احراز هویت
# ========================================

def login_view(request):
    """صفحه ورود"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        print(f"DEBUG: Login attempt for username: {username}")
        
        # از تابع authenticate جنگو استفاده می‌کنیم
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # اگر authenticate موفق بود، کاربر را لاگین می‌کنیم
            login(request, user)
            print(f"DEBUG: Login successful for user: {user.name}")
            messages.success(request, f'خوش آمدید {user.name}!')
            print(f"DEBUG: Redirecting to home page")
            return redirect('home')
        else:
            print(f"DEBUG: Login failed for username: {username}")
            messages.error(request, 'نام کاربری یا رمز عبور اشتباه است یا کاربر غیرفعال است.')
    
    # در هر دو حالت GET و POST (در صورت خطا)، لیست کاربران را به تمپلیت ارسال کن
    user_choices = get_active_users_for_login()
    context = {
        'title': 'ورود به سیستم',
        'user_choices': user_choices
    }
    return render(request, 'login.html', context)


def logout_view(request):
    """خروج از سیستم"""
    logout(request)  # از تابع logout جنگو استفاده کن
    messages.success(request, 'خروج موفقیت‌آمیز')
    return redirect('login')


# ========================================
# VIEW های مدیریت کاربران
# ========================================

@login_required
def user_list(request):
    """لیست کاربران"""
    users = Users.objects.all()
    context = {
        'users': users,
        'title': 'لیست کاربران'
    }
    return render(request, 'accounting/user/list.html', context)


@login_required
def debug_passwords(request):
    """دیباگ رمزهای عبور"""
    from .utils import debug_passwords
    debug_info = debug_passwords()
    context = {
        'debug_info': debug_info,
        'title': 'دیباگ رمزهای عبور'
    }
    return render(request, 'accounting/user/debug_passwords.html', context)


@login_required
def test_password_formats(request):
    """تست فرمت‌های رمز عبور"""
    from .utils import test_password_formats
    test_results = test_password_formats()
    context = {
        'test_results': test_results,
        'title': 'تست فرمت‌های رمز عبور'
    }
    return render(request, 'accounting/user/test_passwords.html', context)


@login_required
def export_users_passwords(request):
    """صادر کردن لیست کاربران"""
    from .utils import export_users_to_excel
    return export_users_to_excel(request)


