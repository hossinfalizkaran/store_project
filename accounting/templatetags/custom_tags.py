from django import template
from django.template.defaultfilters import floatformat, date

register = template.Library()

@register.filter
def get_attribute(obj, attr_name):
    """
    فیلتر سفارشی برای دریافت مقدار یک attribute از یک آبجکت
    """
    try:
        value = getattr(obj, attr_name, '')
        
        # اگر مقدار None است، رشته خالی برگردان
        if value is None:
            return '-'
        
        # اگر فیلد تاریخ است، فرمت مناسب برگردان
        if hasattr(value, 'strftime'):
            return date(value, 'Y/m/d')
        
        # اگر عدد اعشاری است، فرمت مناسب برگردان
        if isinstance(value, (int, float)):
            return floatformat(value, 0)
        
        return str(value)
    except Exception:
        return '-' 