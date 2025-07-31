from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import (
    FactFo, Kharid, ChequesRecieve, ChequePay,
    Perinf, Goodinf, Sanad, SanadDetail
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
            'code': 'شماره فاکتور',
            'shakhs_code': 'مشتری',
            'tarikh': 'تاریخ',
            'sharh': 'شرح'
        }


class SaleItemForm(forms.Form):
    """فرم آیتم فاکتور فروش"""
    good_code = forms.ModelChoiceField(
        queryset=Goodinf.objects.filter(active=True),
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
        label='تخفیف %',
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
        fields = ['code', 'shakhs_code', 'date', 'sharh']
        widgets = {
            'code': forms.NumberInput(attrs={'class': 'form-control'}),
            'shakhs_code': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'sharh': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'code': 'شماره فاکتور',
            'shakhs_code': 'تامین‌کننده',
            'date': 'تاریخ',
            'sharh': 'شرح'
        }


class PurchaseItemForm(forms.Form):
    """فرم آیتم فاکتور خرید"""
    good_code = forms.ModelChoiceField(
        queryset=Goodinf.objects.filter(active=True),
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
            'description': 'شرح',
            'percode': 'صاحب چک'
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
        max_length=500,
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
            'description': 'شرح',
            'percode': 'ذینفع'
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
        queryset=Perinf.objects.filter(type=1),
        label='مشتری',
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    status = forms.ChoiceField(
        choices=[(1, 'فعال'), (0, 'غیرفعال')],
        label='وضعیت',
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )


class InventorySearchForm(forms.Form):
    """فرم جستجو در موجودی انبار"""
    good = forms.ModelChoiceField(
        queryset=Goodinf.objects.filter(active=True),
        label='کالا',
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    store = forms.ChoiceField(
        choices=[],  # باید از مدل Store پر شود
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
        choices=[
            ('daily', 'روزانه'),
            ('weekly', 'هفتگی'),
            ('monthly', 'ماهانه'),
            ('yearly', 'سالانه')
        ],
        label='گروه‌بندی',
        widget=forms.Select(attrs={'class': 'form-control'})
    ) 