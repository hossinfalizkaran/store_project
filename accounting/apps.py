from django.apps import AppConfig


class AccountingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounting'
    verbose_name = 'حسابداری'
    
    def ready(self):
        """
        این متد زمانی که app بارگذاری می‌شود اجرا می‌شود
        می‌توانید signal ها را اینجا ثبت کنید
        """
        try:
            import accounting.signals
        except ImportError:
            pass
