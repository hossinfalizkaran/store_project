from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import (
    FactFo, FactFoDetail, Kharid, ChequesRecieve, ChequePay,
    Perinf, Goodinf, Sanad, SanadDetail, Pergrp,
    Goodgrps, Units, Stores
)


# ========================================
# فرم‌های فروش
# ========================================

class SaleForm(ModelForm):
    """فرم اصلی فاکتور فروش"""
    class Meta:
        model = FactFo
        fields = ['code', 'shakhs_code', 'tarikh', 'sharh']
        widgets = {
            'code': forms.NumberInput(attrs={'class': 'form-control'}),
            'shakhs_code': forms.Select(attrs={'class': 'form-control'}),
            'tarikh': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'sharh': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'code': 'کد فاکتور',
            'shakhs_code': 'مشتری',
            'tarikh': 'تاریخ',
            'sharh': 'شرح',
        }


class SaleItemForm(forms.Form):
    """فرم آیتم فاکتور فروش"""
    good_code = forms.ModelChoiceField(
        queryset=Goodinf.objects.filter(status=0),  # فقط کالاهای فعال
        label='کالا',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    quantity = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label='تعداد',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    unit_price = forms.DecimalField(
        max_digits=15,
        decimal_places=2,
        label='قیمت واحد',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    discount = forms.DecimalField(
        max_digits=5,
        decimal_places=2,
        label='تخفیف (%)',
        required=False,
        initial=0,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )


# ========================================
# فرم‌های خرید
# ========================================

class PurchaseForm(ModelForm):
    """فرم اصلی فاکتور خرید"""
    class Meta:
        model = Kharid
        fields = ['code', 'shakhs_code', 'tarikh', 'sharh']
        widgets = {
            'code': forms.NumberInput(attrs={'class': 'form-control'}),
            'shakhs_code': forms.Select(attrs={'class': 'form-control'}),
            'tarikh': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'sharh': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'code': 'کد فاکتور',
            'shakhs_code': 'فروشنده',
            'tarikh': 'تاریخ',
            'sharh': 'شرح',
        }


class PurchaseItemForm(forms.Form):
    """فرم آیتم فاکتور خرید"""
    good_code = forms.ModelChoiceField(
        queryset=Goodinf.objects.filter(status=0),  # فقط کالاهای فعال
        label='کالا',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    quantity = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label='تعداد',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    unit_price = forms.DecimalField(
        max_digits=15,
        decimal_places=2,
        label='قیمت واحد',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    discount = forms.DecimalField(
        max_digits=5,
        decimal_places=2,
        label='تخفیف (%)',
        required=False,
        initial=0,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )


# ========================================
# فرم‌های چک دریافتی
# ========================================

class ChequeReceiveForm(ModelForm):
    """فرم چک دریافتی"""
    class Meta:
        model = ChequesRecieve
        fields = [
            'chequeid', 'chequedate', 'cost', 'bankname', 
            'bankbranch', 'accountid', 'description', 'percode'
        ]
        widgets = {
            'chequeid': forms.TextInput(attrs={'class': 'form-control'}),
            'chequedate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'bankname': forms.TextInput(attrs={'class': 'form-control'}),
            'bankbranch': forms.TextInput(attrs={'class': 'form-control'}),
            'accountid': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'percode': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'chequeid': 'شماره چک',
            'chequedate': 'تاریخ چک',
            'cost': 'مبلغ',
            'bankname': 'نام بانک',
            'bankbranch': 'شعبه',
            'accountid': 'شماره حساب',
            'description': 'توضیحات',
            'percode': 'شخص',
        }


class ChequeStatusForm(forms.Form):
    """فرم تغییر وضعیت چک"""
    STATUS_CHOICES = [
        (1, 'در انتظار وصول'),
        (2, 'وصول شده'),
        (3, 'برگشت خورده'),
        (4, 'خرج شده')
    ]
    
    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        label='وضعیت جدید',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    location = forms.CharField(
        max_length=50,
        label='محل',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    comment = forms.CharField(
        max_length=200,
        label='توضیحات',
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
    )


# ========================================
# فرم‌های چک پرداختی
# ========================================

class ChequePayForm(ModelForm):
    """فرم چک پرداختی"""
    class Meta:
        model = ChequePay
        fields = [
            'chequeid', 'chequedate', 'cost', 'bankcode', 
            'description', 'percode'
        ]
        widgets = {
            'chequeid': forms.TextInput(attrs={'class': 'form-control'}),
            'chequedate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'bankcode': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'percode': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'chequeid': 'شماره چک',
            'chequedate': 'تاریخ چک',
            'cost': 'مبلغ',
            'bankcode': 'بانک',
            'description': 'توضیحات',
            'percode': 'شخص',
        }


# ========================================
# فرم‌های جستجو
# ========================================

class SaleSearchForm(forms.Form):
    """فرم جستجو در فاکتورهای فروش"""
    date_from = forms.DateField(
        label='از تاریخ',
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    date_to = forms.DateField(
        label='تا تاریخ',
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    customer = forms.ModelChoiceField(
        queryset=Perinf.objects.filter(status=0),  # فقط اشخاص فعال
        label='مشتری',
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    status = forms.ChoiceField(
        choices=[('', 'همه'), ('1', 'فروش'), ('2', 'برگشت')],
        label='نوع',
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )


class InventorySearchForm(forms.Form):
    """فرم جستجو در موجودی انبار"""
    good = forms.ModelChoiceField(
        queryset=Goodinf.objects.filter(status=0),  # فقط کالاهای فعال
        label='کالا',
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    store = forms.ChoiceField(
        choices=[('', 'همه انبارها')],
        label='انبار',
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )


# ========================================
# فرم‌های گزارش‌گیری
# ========================================

class FinancialReportForm(forms.Form):
    """فرم گزارش مالی"""
    REPORT_TYPES = [
        ('profit_loss', 'سود و زیان'),
        ('balance_sheet', 'ترازنامه'),
        ('cash_flow', 'جریان نقدی'),
        ('aging', 'سن بدهی')
    ]
    
    report_type = forms.ChoiceField(
        choices=REPORT_TYPES,
        label='نوع گزارش',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    date_from = forms.DateField(
        label='از تاریخ',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    date_to = forms.DateField(
        label='تا تاریخ',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    group_by = forms.ChoiceField(
        choices=[('customer', 'مشتری'), ('product', 'کالا'), ('date', 'تاریخ')],
        label='گروه‌بندی',
        widget=forms.Select(attrs={'class': 'form-control'})
    )


class PersonForm(forms.ModelForm):
    # فیلد گروه را به صورت دستی تعریف می‌کنیم تا کنترل کامل روی آن داشته باشیم
    grpcode = forms.ModelChoiceField(
        queryset=Pergrp.objects.using('legacy').all(),
        required=False, # این فیلد اختیاری است
        label="گروه شخص",
        widget=forms.Select(attrs={'class': 'form-select'}),
        empty_label="--- بدون گروه ---"
    )

    class Meta:
        model = Perinf
        # **نکته مهم:** 'grpcode' از این لیست حذف شده چون به صورت دستی تعریف شده
        fields = [
            'name', 'lname', 'tel1', 'mobile', 'addr1', 
            'email', 'credit', 'status', 'comment', 'identifier', 'economicno'
        ]
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'lname': forms.TextInput(attrs={'class': 'form-control'}),
            'tel1': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'addr1': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'credit': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'identifier': forms.TextInput(attrs={'class': 'form-control'}),
            'economicno': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'name': 'نام',
            'lname': 'نام خانوادگی',
            'tel1': 'تلفن',
            'mobile': 'موبایل',
            'addr1': 'آدرس',
            'email': 'ایمیل',
            'credit': 'سقف اعتبار',
            'status': 'وضعیت',
            'comment': 'توضیحات',
            'identifier': 'شناسه ملی/کد ملی',
            'economicno': 'کد اقتصادی',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # فقط نام خانوادگی اجباری است
        self.fields['lname'].required = True
        
        # تنظیم choices برای فیلد status
        self.fields['status'].widget.choices = [
            (0, 'فعال'),
            (1, 'غیرفعال'),
            (2, 'موقتا غیرفعال')
        ]


# فرم کالا (GoodForm) را هم برای مراحل بعدی اضافه می‌کنیم
class GoodForm(forms.ModelForm):
    class Meta:
        model = Goodinf
        fields = [
            'name', 'abbname', 'grpcode', 'unit', 'unit2', 'store',
            'consumerprice', 'status', 'comment', 'taxexempt', 'chargeexempt'
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'abbname': forms.TextInput(attrs={'class': 'form-control'}),
            'grpcode': forms.Select(attrs={'class': 'form-select'}),
            'unit': forms.Select(attrs={'class': 'form-select'}),
            'unit2': forms.Select(attrs={'class': 'form-select'}),
            'store': forms.Select(attrs={'class': 'form-select'}),
            'consumerprice': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'taxexempt': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'chargeexempt': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

        labels = {
            'name': 'نام کالا/خدمت',
            'abbname': 'نام اختصاری',
            'grpcode': 'گروه کالا',
            'unit': 'واحد اصلی',
            'unit2': 'واحد فرعی',
            'store': 'انبار پیش‌فرض',
            'consumerprice': 'قیمت مصرف‌کننده',
            'status': 'وضعیت',
            'comment': 'توضیحات',
            'taxexempt': 'معاف از مالیات',
            'chargeexempt': 'معاف از عوارض',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # فقط نام کالا اجباری است
        self.fields['name'].required = True
        
        # تنظیم فیلدهای ForeignKey به صورت اختیاری
        self.fields['grpcode'].required = False
        self.fields['grpcode'].queryset = Goodgrps.objects.using('legacy').all()
        self.fields['grpcode'].empty_label = "--- بدون گروه ---"
        
        self.fields['unit'].required = False
        self.fields['unit'].queryset = Units.objects.using('legacy').all()
        self.fields['unit'].empty_label = "--- بدون واحد ---"
        
        self.fields['unit2'].required = False
        self.fields['unit2'].queryset = Units.objects.using('legacy').all()
        self.fields['unit2'].empty_label = "--- بدون واحد فرعی ---"
        
        self.fields['store'].required = False
        self.fields['store'].queryset = Stores.objects.using('legacy').all()
        self.fields['store'].empty_label = "--- بدون انبار ---"
        
        # سایر فیلدهایی که در مدل blank=True هستند را اختیاری می‌کنیم
        for field_name, field in self.fields.items():
            if field_name != 'name':
                model_field = self.Meta.model._meta.get_field(field_name)
                if model_field.blank:
                    field.required = False

        # تنظیم choices برای فیلد status
        self.fields['status'].widget.choices = [
            (0, 'فعال'),
            (1, 'غیرفعال')
        ]


# ========================================
# فرم‌های فاکتور فروش
# ========================================

class SaleInvoiceForm(forms.ModelForm):
    """فرم اصلی فاکتور فروش"""
    class Meta:
        model = FactFo
        fields = [
            'shakhs_code', 'visitor_code', 'tarikh', 'sharh', 
            'takhfif', 'mablagh_factor'
        ]
        widgets = {
            'shakhs_code': forms.Select(attrs={
                'class': 'form-select',
                'data-placeholder': 'مشتری را انتخاب کنید...'
            }),
            'visitor_code': forms.Select(attrs={
                'class': 'form-select',
                'data-placeholder': 'ویزیتور را انتخاب کنید...'
            }),
            'tarikh': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'sharh': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'شرح فاکتور...'
            }),
            'takhfif': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0',
                'placeholder': '0'
            }),
            'mablagh_factor': forms.NumberInput(attrs={
                'class': 'form-control',
                'readonly': True,
                'placeholder': '0'
            }),
        }
        labels = {
            'shakhs_code': 'مشتری',
            'visitor_code': 'ویزیتور',
            'tarikh': 'تاریخ فاکتور',
            'sharh': 'شرح',
            'takhfif': 'تخفیف کلی (%)',
            'mablagh_factor': 'جمع کل فاکتور',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # فیلتر کردن مشتریان فعال
        self.fields['shakhs_code'].queryset = Perinf.objects.using('legacy').filter(status=0)
        self.fields['shakhs_code'].empty_label = "--- مشتری را انتخاب کنید ---"
        
        # فیلتر کردن ویزیتورهای فعال
        self.fields['visitor_code'].queryset = Perinf.objects.using('legacy').filter(status=0)
        self.fields['visitor_code'].empty_label = "--- ویزیتور را انتخاب کنید ---"
        
        # تنظیم تاریخ پیش‌فرض به امروز
        if not self.instance.pk:  # فقط برای فرم جدید
            from datetime import date
            self.fields['tarikh'].initial = date.today()


class SaleInvoiceDetailForm(forms.ModelForm):
    """فرم جزئیات فاکتور فروش"""
    class Meta:
        model = FactFoDetail
        fields = [
            'kala_code', 'an_code', 'meghdar', 'naghdi', 
            'sharh'
        ]
        widgets = {
            'kala_code': forms.Select(attrs={
                'class': 'form-select good-select',
                'data-placeholder': 'کالا را انتخاب کنید...'
            }),
            'an_code': forms.Select(attrs={
                'class': 'form-select store-select'
            }),
            'meghdar': forms.NumberInput(attrs={
                'class': 'form-control quantity-input',
                'step': '0.01',
                'min': '0.01',
                'placeholder': '0'
            }),
            'naghdi': forms.NumberInput(attrs={
                'class': 'form-control price-input',
                'step': '0.01',
                'min': '0',
                'placeholder': '0'
            }),
            'sharh': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'شرح ردیف...'
            }),
        }
        labels = {
            'kala_code': 'کالا',
            'an_code': 'انبار',
            'meghdar': 'مقدار',
            'naghdi': 'فی فروش',
            'sharh': 'شرح',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # فیلتر کردن کالاهای فعال
        self.fields['kala_code'].queryset = Goodinf.objects.using('legacy').filter(status=0)
        self.fields['kala_code'].empty_label = "--- کالا را انتخاب کنید ---"
        
        # فیلتر کردن انبارهای فعال
        self.fields['an_code'].queryset = Stores.objects.using('legacy').all()
        self.fields['an_code'].empty_label = "--- انبار را انتخاب کنید ---"


# ایجاد FormSet برای جزئیات فاکتور
SaleInvoiceDetailFormSet = inlineformset_factory(
    FactFo,
    FactFoDetail,
    form=SaleInvoiceDetailForm,
    extra=1,  # تعداد ردیف‌های خالی پیش‌فرض
    can_delete=True,  # امکان حذف ردیف‌ها
    min_num=1,  # حداقل یک ردیف
    max_num=50,  # حداکثر 50 ردیف
) 