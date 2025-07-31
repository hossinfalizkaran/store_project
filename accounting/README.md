# سیستم حسابداری - Accounting App

## معرفی

این app برای مدیریت عملیات حسابداری در سیستم Django طراحی شده است. این سیستم بر اساس پایگاه داده موجود و با رعایت قوانین حسابداری دوطرفه عمل می‌کند.

## موجودیت‌های اصلی

### 1. اشخاص (Perinf)
- مشتریان (type=1)
- تامین‌کنندگان (type=2)
- ویزیتورها (type=3)

### 2. کالاها و خدمات (Goodinf)
- مدیریت موجودی
- قیمت‌گذاری
- واحدهای اندازه‌گیری

### 3. اسناد حسابداری (Sanad & SanadDetail)
- تمام عملیات مالی به اینجا ختم می‌شود
- رعایت اصل دوطرفه
- انواع مختلف سند (فروش، خرید، چک، نقدی)

### 4. کاردکس انبار (Kardex)
- تمام عملیات انبارداری به اینجا ختم می‌شود
- ورودی و خروجی کالاها
- محاسبه موجودی

## فلوچارت‌های اصلی

### فلوچارت فروش
1. ثبت `FactFo` (فاکتور فروش)
2. ایجاد رکورد خروجی در `Kardex`
3. ایجاد `Sanad` و `SanadDetail` (بدهکاری مشتری، بستانکاری فروش)
4. ثبت پرداخت نقدی در `GetRecieve` (در صورت وجود)

### فلوچارت خرید
1. ثبت `Kharid` (فاکتور خرید)
2. ایجاد رکورد ورودی در `Kardex`
3. ایجاد `Sanad` و `SanadDetail` (بدهکاری خرید، بستانکاری تامین‌کننده)

### فلوچارت چک
#### چک‌های دریافتی
1. ثبت در `ChequesRecieve`
2. ثبت لاگ در `Chequerecievelog`
3. تغییر وضعیت (وصول، برگشت، خرج)
4. ایجاد سند حسابداری در صورت وصول

#### چک‌های پرداختی
1. ثبت در `ChequePay`
2. ثبت لاگ در `ChequepayLog`
3. ایجاد سند حسابداری (بدهکاری تامین‌کننده، بستانکاری چک‌های پرداختی)

## ساختار فایل‌ها

### views.py
- View های اصلی برای عملیات فروش، خرید و چک
- API endpoints برای AJAX
- مدیریت فرم‌ها و اعتبارسنجی

### forms.py
- فرم‌های Django برای ورود داده
- اعتبارسنجی فرم‌ها
- فرم‌های جستجو و گزارش‌گیری

### utils.py
- توابع کمکی برای محاسبات
- توابع ایجاد اسناد حسابداری
- توابع اعتبارسنجی
- توابع گزارش‌گیری

### signals.py
- مدیریت رویدادها (events)
- ایجاد خودکار اسناد حسابداری
- ثبت لاگ‌ها
- حذف رکوردهای مرتبط

### admin.py
- تنظیمات پنل ادمین
- نمایش و ویرایش مدل‌ها
- فیلترها و جستجو

## نحوه استفاده

### 1. نصب و تنظیم
```python
# در settings.py
INSTALLED_APPS = [
    ...
    'accounting',
]

# در urls.py اصلی
urlpatterns = [
    ...
    path('accounting/', include('accounting.urls')),
]
```

### 2. ایجاد فاکتور فروش
```python
from accounting.views import sales_create

# استفاده از view
response = sales_create(request)
```

### 3. ایجاد چک دریافتی
```python
from accounting.models import ChequesRecieve

cheque = ChequesRecieve.objects.create(
    chequeid='123456',
    chequedate='2024/02/01',
    cost=Decimal('1000000'),
    bankname='ملت',
    percode=customer_code,
    status=1,
    usercreated=user_id,
    owner=user_id
)
```

### 4. محاسبه موجودی
```python
from accounting.utils import get_inventory_balance

balance = get_inventory_balance(good_code=1, store_code=1)
```

## قوانین مهم

### 1. اصل دوطرفه
- هر سند حسابداری باید حداقل دو ردیف داشته باشد
- جمع بدهکاری‌ها = جمع بستانکاری‌ها

### 2. ترتیب عملیات
- ابتدا فاکتور ثبت می‌شود
- سپس کاردکس ایجاد می‌شود
- در نهایت سند حسابداری ثبت می‌شود

### 3. مدیریت چک
- هر تغییر وضعیت چک باید لاگ شود
- وصول چک نیاز به سند حسابداری مجزا دارد

### 4. امنیت
- تمام عملیات در transaction انجام می‌شود
- کاربر ایجاد کننده ثبت می‌شود
- تاریخ و زمان ثبت می‌شود

## API Endpoints

### فروش
- `GET /accounting/sales/` - لیست فاکتورهای فروش
- `GET /accounting/sales/create/` - فرم ایجاد فاکتور
- `POST /accounting/sales/create/` - ایجاد فاکتور
- `GET /accounting/sales/<id>/` - جزئیات فاکتور

### خرید
- `GET /accounting/purchase/` - لیست فاکتورهای خرید
- `GET /accounting/purchase/create/` - فرم ایجاد فاکتور
- `POST /accounting/purchase/create/` - ایجاد فاکتور

### چک
- `GET /accounting/cheque/receive/` - لیست چک‌های دریافتی
- `POST /accounting/cheque/receive/create/` - ثبت چک دریافتی
- `POST /accounting/cheque/receive/<id>/status/` - تغییر وضعیت چک

### API
- `GET /accounting/api/good-info/` - اطلاعات کالا
- `GET /accounting/api/person-info/` - اطلاعات شخص

## تست‌ها

برای اجرای تست‌ها:
```bash
python manage.py test accounting
```

## نکات مهم

1. **مدیریت خطا**: تمام عملیات در try-catch انجام می‌شود
2. **اعتبارسنجی**: داده‌های ورودی اعتبارسنجی می‌شوند
3. **لاگ**: تمام عملیات مهم لاگ می‌شوند
4. **امنیت**: دسترسی‌ها کنترل می‌شود
5. **عملکرد**: از database transaction استفاده می‌شود

## توسعه آینده

1. اضافه کردن گزارش‌های پیشرفته
2. پشتیبانی از ارزهای مختلف
3. سیستم اعلان‌ها
4. API RESTful کامل
5. سیستم مجوزها و دسترسی‌ها 