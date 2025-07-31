# accounting/admin.py

from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import (
    Perinf, Goodinf, Sanad, SanadDetail, Kardex,
    FactFo, Kharid, ChequesRecieve, ChequePay,
    GetRecieve, Bank, Staff
)


# ========================================
# Admin برای اشخاص
# ========================================

@admin.register(Perinf)
class PerinfAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'tel1', 'grpcode', 'status']
    list_filter = ['grpcode', 'status']
    search_fields = ['name', 'tel1', 'code']
    list_per_page = 50
    
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('code', 'name', 'grpcode', 'status')
        }),
        ('اطلاعات تماس', {
            'fields': ('tel1', 'tel2', 'fax', 'mobile', 'email')
        }),
        ('آدرس', {
            'fields': ('addr1', 'comment')
        }),
        ('اطلاعات مالی', {
            'fields': ('credit', 'vouchercode')
        })
    )


# ========================================
# Admin برای کالاها
# ========================================

@admin.register(Goodinf)
class GoodinfAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'consumerprice', 'unit', 'status']
    list_filter = ['status', 'unit']
    search_fields = ['name', 'code']
    list_per_page = 50
    
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('code', 'name', 'status')
        }),
        ('قیمت و واحد', {
            'fields': ('consumerprice', 'unit')
        }),
        ('اطلاعات تکمیلی', {
            'fields': ('comment', 'grpcode')
        })
    )


# ========================================
# Admin برای اسناد حسابداری
# ========================================

class SanadDetailInline(admin.TabularInline):
    model = SanadDetail
    extra = 1
    fields = ['radif', 'kol', 'moin', 'sharh', 'bed', 'bes']
    fk_name = 'sanad'


@admin.register(Sanad)
class SanadAdmin(admin.ModelAdmin):
    list_display = ['sanadid', 'code', 'tarikh', 'sharh', 'status', 'usercreated']
    list_filter = ['status', 'tarikh']
    search_fields = ['code', 'sharh']
    list_per_page = 50
    inlines = [SanadDetailInline]
    
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('code', 'tarikh', 'sharh')
        }),
        ('وضعیت', {
            'fields': ('status', 'usercreated', 'createddate')
        })
    )


# ========================================
# Admin برای کاردکس
# ========================================

@admin.register(Kardex)
class KardexAdmin(admin.ModelAdmin):
    list_display = ['radif', 'code', 'type', 'kala', 'tedad', 'amount', 'date']
    list_filter = ['type', 'status']
    search_fields = ['code', 'kala']
    list_per_page = 50
    
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('code', 'radif', 'type', 'kala')
        }),
        ('مقادیر', {
            'fields': ('tedad', 'amount', 'tedad2')
        }),
        ('اطلاعات تکمیلی', {
            'fields': ('date', 'status', 'sanad_code')
        })
    )


# ========================================
# Admin برای فاکتورهای فروش
# ========================================

@admin.register(FactFo)
class FactFoAdmin(admin.ModelAdmin):
    list_display = ['code', 'shakhs_code', 'tarikh', 'sharh', 'status', 'usercreated']
    list_filter = ['status', 'tarikh']
    search_fields = ['code', 'sharh']
    list_per_page = 50
    
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('code', 'shakhs_code', 'tarikh')
        }),
        ('جزئیات', {
            'fields': ('sharh', 'status')
        }),
        ('اطلاعات کاربر', {
            'fields': ('usercreated', 'createddate', 'createdtime')
        })
    )


# ========================================
# Admin برای فاکتورهای خرید
# ========================================

@admin.register(Kharid)
class KharidAdmin(admin.ModelAdmin):
    list_display = ['code', 'shakhs_code', 'tarikh', 'sharh', 'status', 'usercreated']
    list_filter = ['status', 'tarikh']
    search_fields = ['code', 'sharh']
    list_per_page = 50
    
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('code', 'shakhs_code', 'tarikh')
        }),
        ('جزئیات', {
            'fields': ('sharh', 'status')
        }),
        ('اطلاعات کاربر', {
            'fields': ('usercreated', 'createddate', 'createdtime')
        })
    )


# ========================================
# Admin برای چک‌های دریافتی
# ========================================

@admin.register(ChequesRecieve)
class ChequesRecieveAdmin(admin.ModelAdmin):
    list_display = ['id', 'chequeid', 'chequedate', 'cost', 'bankname', 'status', 'percode']
    list_filter = ['status', 'chequedate']
    search_fields = ['chequeid', 'bankname']
    list_per_page = 50
    
    fieldsets = (
        ('اطلاعات چک', {
            'fields': ('chequeid', 'chequedate', 'cost')
        }),
        ('اطلاعات بانک', {
            'fields': ('bankname', 'bankbranch', 'accountid')
        }),
        ('اطلاعات شخص', {
            'fields': ('percode', 'description')
        }),
        ('وضعیت', {
            'fields': ('status', 'usercreated', 'createddate')
        })
    )


# ========================================
# Admin برای چک‌های پرداختی
# ========================================

@admin.register(ChequePay)
class ChequePayAdmin(admin.ModelAdmin):
    list_display = ['id', 'chequeid', 'chequedate', 'cost', 'bankcode', 'status', 'percode']
    list_filter = ['status', 'chequedate']
    search_fields = ['chequeid']
    list_per_page = 50
    
    fieldsets = (
        ('اطلاعات چک', {
            'fields': ('chequeid', 'chequedate', 'cost')
        }),
        ('اطلاعات بانک', {
            'fields': ('bankcode', 'description')
        }),
        ('اطلاعات شخص', {
            'fields': ('percode',)
        }),
        ('وضعیت', {
            'fields': ('status', 'usercreated', 'createddate')
        })
    )


# ========================================
# Admin برای بانک‌ها
# ========================================

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'shobe', 'tel', 'mogodi']
    list_filter = ['code_m']
    search_fields = ['name', 'shobe']
    list_per_page = 50
    
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('code', 'name', 'shobe')
        }),
        ('اطلاعات تماس', {
            'fields': ('tel', 'fax')
        }),
        ('اطلاعات مالی', {
            'fields': ('mogodi', 'comment')
        })
    )


# ========================================
# Admin برای کارمندان
# ========================================

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'lastname', 'personnelcode', 'department', 'job']
    list_filter = ['staffgroup', 'sex', 'ismarried']
    search_fields = ['name', 'lastname', 'personnelcode']
    list_per_page = 50
    
    fieldsets = (
        ('اطلاعات شخصی', {
            'fields': ('code', 'name', 'lastname', 'sex', 'ismarried')
        }),
        ('اطلاعات شغلی', {
            'fields': ('staffgroup', 'personnelcode', 'department', 'job')
        }),
        ('اطلاعات تماس', {
            'fields': ('tel1', 'tel2', 'mob', 'email')
        }),
        ('آدرس', {
            'fields': ('add1', 'add2', 'postcode')
        }),
        ('اطلاعات تکمیلی', {
            'fields': ('comment', 'picture')
        })
    )


# ========================================
# Admin برای دریافت‌ها و پرداخت‌ها
# ========================================

@admin.register(GetRecieve)
class GetRecieveAdmin(admin.ModelAdmin):
    list_display = ['code', 'type', 'percode', 'date', 'amount', 'comment']
    list_filter = ['type', 'date']
    search_fields = ['code', 'comment']
    list_per_page = 50
    
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('code', 'type', 'percode', 'date')
        }),
        ('جزئیات', {
            'fields': ('amount', 'comment', 'status')
        }),
        ('اطلاعات کاربر', {
            'fields': ('usercreated', 'createddate', 'createdtime')
        })
    )


# ========================================
# تنظیمات کلی Admin
# ========================================

admin.site.site_header = "سیستم حسابداری"
admin.site.site_title = "پنل مدیریت"
admin.site.index_title = "مدیریت سیستم حسابداری"

# ثبت مدل‌های دیگر بدون تنظیمات خاص
admin.site.register(SanadDetail)