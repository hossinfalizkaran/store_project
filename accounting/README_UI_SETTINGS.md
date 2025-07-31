# سیستم مدیریت تنظیمات UI (UI Settings Management)

## مقدمه

این سیستم امکان مدیریت داینامیک تنظیمات نمایش (UI Settings) را برای کاربران فراهم می‌کند. تمام تنظیمات ظاهری، نحوه مرتب‌سازی لیست‌ها، ستون‌های قابل نمایش در جداول و موارد مشابه، از دیتابیس و عمدتاً از جدول `Settings` خوانده می‌شوند.

## قانون اصلی

**رابط کاربری باید داینامیک باشد. قبل از رندر کردن هر لیست یا جدولی، ابتدا تنظیمات ذخیره شده برای آن بخش را از دیتابیس بخوان و تمپلیت را بر اساس آن تنظیمات رندر کن.**

## ساختار سیستم

### 1. مدل Settings

جدول `Settings` شامل فیلدهای زیر است:

- `category`: دسته تنظیمات (مثلاً 3 برای تنظیمات نمایش لیست‌ها)
- `code`: کد تنظیمات (مثلاً 1 برای تنظیمات لیست اشخاص)
- `selected`: مقدار boolean برای تنظیمات دو حالته
- `comment`: مقدار متنی برای تنظیمات پیچیده
- `managetype`: نوع مدیریت (0=عمومی، 1=شخصی)
- `usercode`: کد کاربر (0 برای تنظیمات عمومی)

### 2. شناسه‌های تنظیمات

هر بخش قابل تنظیم در برنامه یک شناسه منحصر به فرد دارد:

| Category | Code | توضیحات |
|----------|------|---------|
| 3 | 1 | تنظیمات مرتب‌سازی لیست اشخاص |
| 3 | 2 | تنظیمات ستون‌های قابل نمایش لیست اشخاص |
| 3 | 3 | نمایش اشخاص غیرفعال |
| 3 | 4 | تعداد آیتم در صفحه لیست اشخاص |
| 3 | 10 | تنظیمات مرتب‌سازی لیست اسناد |
| 3 | 11 | تنظیمات ستون‌های قابل نمایش لیست اسناد |
| 3 | 12 | نمایش اسناد لغو شده |
| 3 | 13 | تعداد آیتم در صفحه لیست اسناد |
| 3 | 20 | تنظیمات مرتب‌سازی لیست فاکتورهای فروش |
| 3 | 21 | تنظیمات ستون‌های قابل نمایش لیست فاکتورهای فروش |
| 3 | 22 | نمایش فاکتورهای لغو شده |
| 3 | 23 | تعداد آیتم در صفحه لیست فاکتورهای فروش |
| 3 | 30 | تنظیمات مرتب‌سازی لیست فاکتورهای خرید |
| 3 | 31 | تنظیمات ستون‌های قابل نمایش لیست فاکتورهای خرید |
| 3 | 32 | نمایش فاکتورهای لغو شده |
| 3 | 33 | تعداد آیتم در صفحه لیست فاکتورهای خرید |
| 3 | 40 | تنظیمات مرتب‌سازی لیست کالاها |
| 3 | 41 | تنظیمات ستون‌های قابل نمایش لیست کالاها |
| 3 | 42 | نمایش کالاهای غیرفعال |
| 3 | 43 | تعداد آیتم در صفحه لیست کالاها |

## توابع اصلی

### 1. دریافت تنظیمات

```python
from accounting.utils import get_setting, get_boolean_setting

# دریافت تنظیم متنی
sort_key = get_setting(user_id, 3, 1, 'code')

# دریافت تنظیم boolean
show_inactive = get_boolean_setting(user_id, 3, 3, False)
```

### 2. ذخیره تنظیمات

```python
from accounting.utils import set_user_setting, set_boolean_setting

# ذخیره تنظیم متنی
set_user_setting(user_id, 3, 1, 'lname,name')

# ذخیره تنظیم boolean
set_boolean_setting(user_id, 3, 3, True)
```

### 3. دریافت تنظیمات کامل لیست

```python
from accounting.utils import get_person_list_settings

settings = get_person_list_settings(user_id)
# Returns: {
#     'sort_key': 'code',
#     'visible_columns': ['code', 'name', 'lname', 'tel1', 'mobile', 'credit'],
#     'show_inactive': False,
#     'page_size': 20
# }
```

## پیاده‌سازی در View ها

### مثال: View لیست اشخاص

```python
@login_required
def person_list(request):
    from .utils import get_person_list_settings, get_list_context
    
    # دریافت تنظیمات لیست برای کاربر
    user_id = request.user.id
    settings_dict = get_person_list_settings(user_id)
    
    # دریافت queryset اصلی
    queryset = Perinf.objects.all()
    
    # اعمال تنظیمات و دریافت context
    context = get_list_context(queryset, settings_dict, request)
    
    # اضافه کردن اطلاعات اضافی
    context.update({
        'title': 'لیست اشخاص',
        'model_name': 'Perinf',
        'get_column_display_name': get_column_display_name,
        'get_column_value': get_column_value,
        'format_column_value': format_column_value,
    })
    
    return render(request, 'accounting/person/list.html', context)
```

## پیاده‌سازی در Template ها

### مثال: Template داینامیک

```html
<table class="person-table">
    <thead>
        <tr>
            {% for column in visible_columns %}
            <th>{{ get_column_display_name|call:column }}</th>
            {% endfor %}
            <th>عملیات</th>
        </tr>
    </thead>
    <tbody>
        {% for person in object_list %}
        <tr>
            {% for column in visible_columns %}
            <td>
                {{ format_column_value|call:get_column_value|call:person|call:column|call:column }}
            </td>
            {% endfor %}
            <td>
                <!-- دکمه‌های عملیات -->
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>
```

## فرایند اولویت‌بندی تنظیمات

1. **تنظیمات شخصی کاربر**: `usercode=user_id, managetype=1`
2. **تنظیمات عمومی سیستم**: `usercode=0, managetype=0`
3. **مقدار پیش‌فرض**: تعریف شده در کد

## مثال داده در جدول Settings

```sql
-- تنظیمات عمومی مرتب‌سازی لیست اشخاص
INSERT INTO Settings (Category, Code, ManageType, UserCode, Comment) 
VALUES (3, 1, 0, 0, 'code');

-- تنظیمات شخصی کاربر شماره 12
INSERT INTO Settings (Category, Code, ManageType, UserCode, Comment) 
VALUES (3, 1, 1, 12, 'lname,name');

-- تنظیمات عمومی ستون‌های قابل نمایش
INSERT INTO Settings (Category, Code, ManageType, UserCode, Comment) 
VALUES (3, 2, 0, 0, 'code,name,lname,tel1,mobile,credit');

-- تنظیمات boolean نمایش اشخاص غیرفعال
INSERT INTO Settings (Category, Code, ManageType, UserCode, Selected) 
VALUES (3, 3, 0, 0, 0);
```

## URL های جدید

```python
# لیست‌های داینامیک با تنظیمات UI
path('person/list/', views.person_list, name='person_list'),
path('person/settings/', views.person_settings, name='person_settings'),
path('sales/list-dynamic/', views.sales_list_dynamic, name='sales_list_dynamic'),
path('purchase/list-dynamic/', views.purchase_list_dynamic, name='purchase_list_dynamic'),
path('sanad/list-dynamic/', views.sanad_list_dynamic, name='sanad_list_dynamic'),
path('good/list-dynamic/', views.good_list_dynamic, name='good_list_dynamic'),
```

## مزایای سیستم

1. **انعطاف‌پذیری**: کاربران می‌توانند تنظیمات شخصی خود را داشته باشند
2. **عملکرد بهتر**: تنظیمات در دیتابیس ذخیره می‌شوند و نیازی به بارگذاری مجدد نیست
3. **قابلیت توسعه**: به راحتی می‌توان تنظیمات جدید اضافه کرد
4. **سازگاری**: با سیستم موجود Mahak سازگار است
5. **امنیت**: تنظیمات شخصی از تنظیمات عمومی جدا هستند

## نکات پیاده‌سازی

1. **Cache کردن**: برای بهبود عملکرد، می‌توان تنظیمات را cache کرد
2. **Validation**: اعتبارسنجی تنظیمات قبل از ذخیره
3. **Backup**: پشتیبان‌گیری از تنظیمات مهم
4. **Migration**: انتقال تنظیمات قدیمی به سیستم جدید
5. **Logging**: ثبت تغییرات تنظیمات برای audit

## توسعه آینده

1. **تنظیمات پیشرفته**: فیلترهای پیچیده، جستجوی پیشرفته
2. **Export/Import**: صادرات و واردات تنظیمات
3. **Template های سفارشی**: امکان ایجاد template های شخصی
4. **API**: ارائه API برای تنظیمات
5. **Dashboard**: داشبورد مدیریت تنظیمات 