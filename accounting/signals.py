from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from django.db import transaction
from django.utils import timezone
from .models import (
    FactFo, Kharid, Sanad, SanadDetail, Kardex,
    ChequesRecieve, ChequePay, GetRecieve
)
from .utils import (
    create_accounting_voucher, create_voucher_detail,
    create_kardex_entry, create_cheque_log
)


# ========================================
# Signal های مربوط به فاکتور فروش
# ========================================

@receiver(post_save, sender=FactFo)
def create_sales_voucher_and_kardex(sender, instance, created, **kwargs):
    """
    هنگام ایجاد فاکتور فروش، سند حسابداری و کاردکس ایجاد می‌شود
    """
    if created and instance.type == 1 and instance.tmp == 0:
        # این signal فقط برای فاکتورهای فروش اصلی اجرا می‌شود
        # جزئیات فاکتور باید از طریق API یا view مدیریت شود
        pass


# ========================================
# Signal های مربوط به فاکتور خرید
# ========================================

@receiver(post_save, sender=Kharid)
def create_purchase_voucher_and_kardex(sender, instance, created, **kwargs):
    """
    هنگام ایجاد فاکتور خرید، سند حسابداری و کاردکس ایجاد می‌شود
    """
    if created and instance.type == 1 and instance.tmp == 0:
        # این signal فقط برای فاکتورهای خرید اصلی اجرا می‌شود
        # جزئیات فاکتور باید از طریق API یا view مدیریت شود
        pass


# ========================================
# Signal های مربوط به چک‌های دریافتی
# ========================================

@receiver(post_save, sender=ChequesRecieve)
def create_received_cheque_log(sender, instance, created, **kwargs):
    """
    هنگام ایجاد چک دریافتی، لاگ ثبت می‌شود
    """
    if created:
        create_cheque_log(
            cheque_id=instance.id,
            status=instance.status,
            entity_code=instance.percode,
            location='ثبت اولیه',
            comment='ثبت چک دریافتی جدید',
            user_id=instance.usercreated,
            owner_id=instance.owner,
            is_receive=True
        )


@receiver(pre_save, sender=ChequesRecieve)
def update_received_cheque_status(sender, instance, **kwargs):
    """
    هنگام تغییر وضعیت چک دریافتی، لاگ و سند حسابداری ایجاد می‌شود
    """
    if instance.pk:  # فقط برای رکوردهای موجود
        try:
            old_instance = ChequesRecieve.objects.get(pk=instance.pk)
            if old_instance.status != instance.status:
                # وضعیت تغییر کرده است
                create_cheque_log(
                    cheque_id=instance.id,
                    status=instance.status,
                    entity_code=instance.percode,
                    location='تغییر وضعیت',
                    comment=f'تغییر وضعیت از {old_instance.status} به {instance.status}',
                    user_id=instance.usermodified or instance.usercreated,
                    owner_id=instance.owner,
                    is_receive=True
                )
                
                # اگر چک وصول شد، سند حسابداری ایجاد کن
                if instance.status == 2:  # وصول شده
                    with transaction.atomic():
                        sanad = create_accounting_voucher(
                            code=instance.id,
                            voucher_type=3,  # وصول چک
                            date=timezone.now().strftime('%Y/%m/%d'),
                            description=f'وصول چک {instance.chequeid}',
                            user_id=instance.usermodified or instance.usercreated,
                            owner_id=instance.owner
                        )
                        
                        # بدهکاری بانک
                        create_voucher_detail(
                            sanad=sanad,
                            row=1,
                            kol=3,  # حساب بانک
                            moin=instance.bankcode if hasattr(instance, 'bankcode') else 1,
                            description=f'وصول چک {instance.chequeid}',
                            debit=instance.cost,
                            credit=0,
                            user_id=instance.usermodified or instance.usercreated
                        )
                        
                        # بستانکاری چک‌های دریافتی
                        create_voucher_detail(
                            sanad=sanad,
                            row=2,
                            kol=5,  # حساب چک‌های دریافتی
                            moin=instance.percode,
                            description=f'وصول چک {instance.chequeid}',
                            debit=0,
                            credit=instance.cost,
                            user_id=instance.usermodified or instance.usercreated
                        )
        except ChequesRecieve.DoesNotExist:
            pass


# ========================================
# Signal های مربوط به چک‌های پرداختی
# ========================================

@receiver(post_save, sender=ChequePay)
def create_paid_cheque_log_and_voucher(sender, instance, created, **kwargs):
    """
    هنگام ایجاد چک پرداختی، لاگ و سند حسابداری ایجاد می‌شود
    """
    if created:
        # ایجاد لاگ
        create_cheque_log(
            cheque_id=instance.id,
            status=instance.status,
            entity_code=instance.percode,
            location='صدور چک',
            comment='صدور چک پرداختی جدید',
            user_id=instance.usercreated,
            owner_id=instance.owner,
            is_receive=False
        )
        
        # ایجاد سند حسابداری
        with transaction.atomic():
            sanad = create_accounting_voucher(
                code=instance.id,
                voucher_type=4,  # صدور چک
                date=timezone.now().strftime('%Y/%m/%d'),
                description=f'صدور چک {instance.chequeid}',
                user_id=instance.usercreated,
                owner_id=instance.owner
            )
            
            # بدهکاری تامین‌کننده
            create_voucher_detail(
                sanad=sanad,
                row=1,
                kol=1,  # حساب تامین‌کنندگان
                moin=instance.percode,
                description=f'بدهکاری تامین‌کننده - چک {instance.chequeid}',
                debit=instance.cost,
                credit=0,
                user_id=instance.usercreated
            )
            
            # بستانکاری چک‌های پرداختی
            create_voucher_detail(
                sanad=sanad,
                row=2,
                kol=6,  # حساب چک‌های پرداختی
                moin=instance.bankcode,
                description=f'صدور چک {instance.chequeid}',
                debit=0,
                credit=instance.cost,
                user_id=instance.usercreated
            )


@receiver(pre_save, sender=ChequePay)
def update_paid_cheque_status(sender, instance, **kwargs):
    """
    هنگام تغییر وضعیت چک پرداختی، لاگ ایجاد می‌شود
    """
    if instance.pk:  # فقط برای رکوردهای موجود
        try:
            old_instance = ChequePay.objects.get(pk=instance.pk)
            if old_instance.status != instance.status:
                # وضعیت تغییر کرده است
                create_cheque_log(
                    cheque_id=instance.id,
                    status=instance.status,
                    entity_code=instance.percode,
                    location='تغییر وضعیت',
                    comment=f'تغییر وضعیت از {old_instance.status} به {instance.status}',
                    user_id=instance.usermodified or instance.usercreated,
                    owner_id=instance.owner,
                    is_receive=False
                )
        except ChequePay.DoesNotExist:
            pass


# ========================================
# Signal های مربوط به دریافت‌ها و پرداخت‌ها
# ========================================

@receiver(post_save, sender=GetRecieve)
def create_cash_voucher(sender, instance, created, **kwargs):
    """
    هنگام ثبت دریافت یا پرداخت نقدی، سند حسابداری ایجاد می‌شود
    """
    if created:
        with transaction.atomic():
            voucher_type = 5 if instance.type == 1 else 6  # 5=دریافت نقدی، 6=پرداخت نقدی
            description = f'{"دریافت" if instance.type == 1 else "پرداخت"} نقدی - {instance.description}'
            
            sanad = create_accounting_voucher(
                code=instance.code,
                voucher_type=voucher_type,
                date=instance.date,
                description=description,
                user_id=instance.usercreated,
                owner_id=instance.owner
            )
            
            if instance.type == 1:  # دریافت
                # بدهکاری صندوق
                create_voucher_detail(
                    sanad=sanad,
                    row=1,
                    kol=7,  # حساب صندوق
                    moin=1,
                    description=description,
                    debit=instance.cost,
                    credit=0,
                    user_id=instance.usercreated
                )
                
                # بستانکاری شخص
                create_voucher_detail(
                    sanad=sanad,
                    row=2,
                    kol=1,  # حساب اشخاص
                    moin=instance.percode,
                    description=description,
                    debit=0,
                    credit=instance.cost,
                    user_id=instance.usercreated
                )
            else:  # پرداخت
                # بدهکاری شخص
                create_voucher_detail(
                    sanad=sanad,
                    row=1,
                    kol=1,  # حساب اشخاص
                    moin=instance.percode,
                    description=description,
                    debit=instance.cost,
                    credit=0,
                    user_id=instance.usercreated
                )
                
                # بستانکاری صندوق
                create_voucher_detail(
                    sanad=sanad,
                    row=2,
                    kol=7,  # حساب صندوق
                    moin=1,
                    description=description,
                    debit=0,
                    credit=instance.cost,
                    user_id=instance.usercreated
                )


# ========================================
# Signal های مربوط به حذف رکوردها
# ========================================

@receiver(post_delete, sender=FactFo)
def delete_sales_related_records(sender, instance, **kwargs):
    """
    هنگام حذف فاکتور فروش، رکوردهای مرتبط نیز حذف می‌شوند
    """
    # حذف کاردکس‌های مرتبط
    Kardex.objects.filter(code=instance.code, type=1).delete()
    
    # حذف اسناد حسابداری مرتبط
    Sanad.objects.filter(code=instance.code, type=1).delete()


@receiver(post_delete, sender=Kharid)
def delete_purchase_related_records(sender, instance, **kwargs):
    """
    هنگام حذف فاکتور خرید، رکوردهای مرتبط نیز حذف می‌شوند
    """
    # حذف کاردکس‌های مرتبط
    Kardex.objects.filter(code=instance.code, type=0).delete()
    
    # حذف اسناد حسابداری مرتبط
    Sanad.objects.filter(code=instance.code, type=2).delete()


@receiver(post_delete, sender=ChequesRecieve)
def delete_received_cheque_related_records(sender, instance, **kwargs):
    """
    هنگام حذف چک دریافتی، لاگ‌های مرتبط نیز حذف می‌شوند
    """
    Chequerecievelog.objects.filter(chequerecieveid=instance.id).delete()


@receiver(post_delete, sender=ChequePay)
def delete_paid_cheque_related_records(sender, instance, **kwargs):
    """
    هنگام حذف چک پرداختی، لاگ‌های مرتبط نیز حذف می‌شوند
    """
    ChequepayLog.objects.filter(chequepayid=instance.id).delete() 