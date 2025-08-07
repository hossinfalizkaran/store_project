# accounting/templatetags/persian_filters.py

from django import template
import jdatetime
from datetime import datetime, timedelta

register = template.Library()

@register.filter
def to_jalali(gregorian_date_str):
    """
    یک تاریخ میلادی (به صورت رشته یا آبجکت) را به تاریخ شمسی تبدیل می‌کند.
    """
    if not gregorian_date_str:
        return ""

    try:
        # اگر ورودی یک رشته است، آن را به آبجکت datetime تبدیل کن
        if isinstance(gregorian_date_str, str):
            # فرمت‌های رایج تاریخ را امتحان کن
            for fmt in ('%Y-%m-%d %H:%M:%S', '%Y-%m-%d', '%Y/%m/%d'):
                try:
                    gregorian_date = datetime.strptime(gregorian_date_str.split('.')[0], fmt)
                    break
                except ValueError:
                    pass
            else:
                 # اگر هیچ فرمتی نخورد، همان رشته را برگردان
                return gregorian_date_str
        else:
            gregorian_date = gregorian_date_str

        # تبدیل به تاریخ شمسی
        jalali_date = jdatetime.datetime.fromgregorian(datetime=gregorian_date)
        return jalali_date.strftime('%Y/%m/%d')
    except (ValueError, TypeError):
        # در صورت بروز هرگونه خطا، مقدار اصلی را برگردان
        return gregorian_date_str

@register.filter
def get_jalali_today(value):
    return jdatetime.date.today().strftime('%Y/%m/%d')

@register.filter
def get_jalali_first_of_month(value):
    return jdatetime.date.today().replace(day=1).strftime('%Y/%m/%d')
    
@register.filter
def get_jalali_first_of_year(value):
    return jdatetime.date.today().replace(day=1, month=1).strftime('%Y/%m/%d')

@register.filter
def get_jalali_days_ago(value, days):
    """تاریخ X روز قبل را به صورت شمسی برمی‌گرداند."""
    try:
        gregorian_ago = datetime.now() - timedelta(days=int(days))
        return jdatetime.date.fromgregorian(date=gregorian_ago).strftime('%Y/%m/%d')
    except:
        return "" 