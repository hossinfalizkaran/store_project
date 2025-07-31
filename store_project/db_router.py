# db_router.py

class LegacyRouter:
    """
    A router to control all database operations on models in the
    'accounting' application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read accounting models go to legacy.
        """
        if model._meta.app_label == 'accounting':
            return 'legacy'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write accounting models go to legacy.
        """
        if model._meta.app_label == 'accounting':
            return 'legacy'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if both models are in the accounting app.
        """
        if (
            obj1._meta.app_label == 'accounting' or
            obj2._meta.app_label == 'accounting'
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the accounting app only appears in the 'legacy'
        database.
        """
        if app_label == 'accounting':
            return db == 'legacy'
        return db == 'default'