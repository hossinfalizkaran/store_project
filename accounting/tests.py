from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from decimal import Decimal
import json

from .models import (
    Perinf, Goodinf, FactFo, Kharid, Sanad, SanadDetail, Kardex,
    ChequesRecieve, ChequePay, GetRecieve
)
from .utils import (
    create_accounting_voucher, create_voucher_detail,
    create_kardex_entry, calculate_total_with_tax,
    calculate_discount, validate_cheque_number
)


# ========================================
# تست‌های مدل‌ها
# ========================================

class PerinfModelTest(TestCase):
    """تست‌های مدل اشخاص"""
    
    def setUp(self):
        """تنظیم داده‌های اولیه"""
        self.person = Perinf.objects.create(
            code=1,
            name='احمد محمدی',
            tel='02112345678',
            type=1,  # مشتری
            active=True
        )
    
    def test_person_creation(self):
        """تست ایجاد شخص"""
        self.assertEqual(self.person.name, 'احمد محمدی')
        self.assertEqual(self.person.type, 1)
        self.assertTrue(self.person.active)
    
    def test_person_str(self):
        """تست نمایش رشته‌ای شخص"""
        self.assertEqual(str(self.person), 'احمد محمدی')


class GoodinfModelTest(TestCase):
    """تست‌های مدل کالاها"""
    
    def setUp(self):
        """تنظیم داده‌های اولیه"""
        self.good = Goodinf.objects.create(
            code=1,
            name='لپ‌تاپ',
            price=Decimal('15000000'),
            unit='عدد',
            active=True
        )
    
    def test_good_creation(self):
        """تست ایجاد کالا"""
        self.assertEqual(self.good.name, 'لپ‌تاپ')
        self.assertEqual(self.good.price, Decimal('15000000'))
        self.assertEqual(self.good.unit, 'عدد')
    
    def test_good_str(self):
        """تست نمایش رشته‌ای کالا"""
        self.assertEqual(str(self.good), 'لپ‌تاپ')


# ========================================
# تست‌های توابع کمکی
# ========================================

class UtilsTest(TestCase):
    """تست‌های توابع کمکی"""
    
    def test_calculate_total_with_tax(self):
        """تست محاسبه مبلغ با مالیات"""
        amount = Decimal('1000000')
        tax_percent = Decimal('9')
        
        base_amount, tax_amount, total = calculate_total_with_tax(amount, tax_percent)
        
        self.assertEqual(base_amount, Decimal('1000000'))
        self.assertEqual(tax_amount, Decimal('90000'))
        self.assertEqual(total, Decimal('1090000'))
    
    def test_calculate_discount(self):
        """تست محاسبه تخفیف"""
        amount = Decimal('1000000')
        discount_percent = Decimal('10')
        
        base_amount, discount_amount, final_amount = calculate_discount(amount, discount_percent)
        
        self.assertEqual(base_amount, Decimal('1000000'))
        self.assertEqual(discount_amount, Decimal('100000'))
        self.assertEqual(final_amount, Decimal('900000'))
    
    def test_validate_cheque_number_valid(self):
        """تست اعتبارسنجی شماره چک معتبر"""
        valid_cheque = '123456'
        self.assertTrue(validate_cheque_number(valid_cheque))
    
    def test_validate_cheque_number_invalid(self):
        """تست اعتبارسنجی شماره چک نامعتبر"""
        invalid_cheques = ['', '12345', '12345678901', 'abc123']
        for cheque in invalid_cheques:
            self.assertFalse(validate_cheque_number(cheque))


# ========================================
# تست‌های View ها
# ========================================

class SalesViewTest(TestCase):
    """تست‌های view های فروش"""
    
    def setUp(self):
        """تنظیم داده‌های اولیه"""
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')
        
        # ایجاد مشتری
        self.customer = Perinf.objects.create(
            code=1,
            name='احمد محمدی',
            type=1,
            active=True
        )
        
        # ایجاد کالا
        self.good = Goodinf.objects.create(
            code=1,
            name='لپ‌تاپ',
            price=Decimal('15000000'),
            unit='عدد',
            active=True
        )
    
    def test_sales_list_view(self):
        """تست نمایش لیست فروش"""
        response = self.client.get(reverse('accounting:sales_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounting/sales/list.html')
    
    def test_sales_create_view_get(self):
        """تست نمایش فرم ایجاد فروش"""
        response = self.client.get(reverse('accounting:sales_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounting/sales/create.html')
    
    def test_sales_create_view_post(self):
        """تست ایجاد فاکتور فروش"""
        data = {
            'code': 1,
            'customer_code': self.customer.code,
            'date': '2024/01/01',
            'description': 'فروش لپ‌تاپ',
            'items': [
                {
                    'row': 1,
                    'good_code': self.good.code,
                    'quantity': 1,
                    'unit_price': 15000000,
                    'total_price': 15000000
                }
            ],
            'cash_payment': 0
        }
        
        response = self.client.post(
            reverse('accounting:sales_create'),
            data=json.dumps(data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertTrue(response_data['success'])


class PurchaseViewTest(TestCase):
    """تست‌های view های خرید"""
    
    def setUp(self):
        """تنظیم داده‌های اولیه"""
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')
        
        # ایجاد تامین‌کننده
        self.supplier = Perinf.objects.create(
            code=2,
            name='شرکت تامین‌کننده',
            type=2,
            active=True
        )
        
        # ایجاد کالا
        self.good = Goodinf.objects.create(
            code=1,
            name='لپ‌تاپ',
            price=Decimal('12000000'),
            unit='عدد',
            active=True
        )
    
    def test_purchase_list_view(self):
        """تست نمایش لیست خرید"""
        response = self.client.get(reverse('accounting:purchase_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounting/purchase/list.html')
    
    def test_purchase_create_view_get(self):
        """تست نمایش فرم ایجاد خرید"""
        response = self.client.get(reverse('accounting:purchase_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounting/purchase/create.html')


class ChequeViewTest(TestCase):
    """تست‌های view های چک"""
    
    def setUp(self):
        """تنظیم داده‌های اولیه"""
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')
        
        # ایجاد شخص
        self.person = Perinf.objects.create(
            code=1,
            name='احمد محمدی',
            type=1,
            active=True
        )
    
    def test_cheque_receive_list_view(self):
        """تست نمایش لیست چک‌های دریافتی"""
        response = self.client.get(reverse('accounting:cheque_receive_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounting/cheque/receive_list.html')
    
    def test_cheque_receive_create_view_get(self):
        """تست نمایش فرم ایجاد چک دریافتی"""
        response = self.client.get(reverse('accounting:cheque_receive_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounting/cheque/receive_create.html')
    
    def test_cheque_pay_list_view(self):
        """تست نمایش لیست چک‌های پرداختی"""
        response = self.client.get(reverse('accounting:cheque_pay_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounting/cheque/pay_list.html')


# ========================================
# تست‌های API
# ========================================

class APITest(TestCase):
    """تست‌های API"""
    
    def setUp(self):
        """تنظیم داده‌های اولیه"""
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')
        
        # ایجاد کالا
        self.good = Goodinf.objects.create(
            code=1,
            name='لپ‌تاپ',
            price=Decimal('15000000'),
            unit='عدد',
            active=True
        )
        
        # ایجاد شخص
        self.person = Perinf.objects.create(
            code=1,
            name='احمد محمدی',
            type=1,
            active=True
        )
    
    def test_get_good_info_api(self):
        """تست API دریافت اطلاعات کالا"""
        response = self.client.get(
            reverse('accounting:get_good_info'),
            {'good_code': self.good.code}
        )
        
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertTrue(response_data['success'])
        self.assertEqual(response_data['good']['name'], 'لپ‌تاپ')
    
    def test_get_person_info_api(self):
        """تست API دریافت اطلاعات شخص"""
        response = self.client.get(
            reverse('accounting:get_person_info'),
            {'person_code': self.person.code}
        )
        
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertTrue(response_data['success'])
        self.assertEqual(response_data['person']['name'], 'احمد محمدی')


# ========================================
# تست‌های یکپارچگی
# ========================================

class IntegrationTest(TestCase):
    """تست‌های یکپارچگی"""
    
    def setUp(self):
        """تنظیم داده‌های اولیه"""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        # ایجاد مشتری
        self.customer = Perinf.objects.create(
            code=1,
            name='احمد محمدی',
            type=1,
            active=True
        )
        
        # ایجاد کالا
        self.good = Goodinf.objects.create(
            code=1,
            name='لپ‌تاپ',
            price=Decimal('15000000'),
            unit='عدد',
            active=True
        )
    
    def test_sales_integration(self):
        """تست یکپارچگی فرآیند فروش"""
        # ایجاد فاکتور فروش
        sale = FactFo.objects.create(
            code=1,
            type=1,
            tmp=0,
            shakhs_code=self.customer.code,
            tarikh='2024/01/01',
            sharh='فروش لپ‌تاپ',
            status=1,
            usercreated=self.user.id,
            createdtime='10:00',
            createddate='2024/01/01',
            owner=self.user.id
        )
        
        # بررسی ایجاد کاردکس
        kardex = Kardex.objects.filter(code=sale.code, type=1).first()
        self.assertIsNotNone(kardex)
        
        # بررسی ایجاد سند حسابداری
        sanad = Sanad.objects.filter(code=sale.code, type=1).first()
        self.assertIsNotNone(sanad)
    
    def test_cheque_integration(self):
        """تست یکپارچگی فرآیند چک"""
        # ایجاد چک دریافتی
        cheque = ChequesRecieve.objects.create(
            chequeid='123456',
            chequedate='2024/02/01',
            cost=Decimal('1000000'),
            bankname='ملت',
            percode=self.customer.code,
            status=1,
            usercreated=self.user.id,
            createdtime='10:00',
            createddate='2024/01/01',
            owner=self.user.id
        )
        
        # بررسی ایجاد لاگ
        log = Chequerecievelog.objects.filter(chequerecieveid=cheque.id).first()
        self.assertIsNotNone(log)
        
        # تغییر وضعیت چک
        cheque.status = 2  # وصول شده
        cheque.save()
        
        # بررسی ایجاد سند حسابداری برای وصول
        sanad = Sanad.objects.filter(code=cheque.id, type=3).first()
        self.assertIsNotNone(sanad)
