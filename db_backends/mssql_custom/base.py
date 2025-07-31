# db_backends/mssql_custom/base.py

from mssql.base import DatabaseWrapper as MssqlDatabaseWrapper
from django.utils.functional import cached_property

class DatabaseWrapper(MssqlDatabaseWrapper):
    """
    This is a custom database backend that inherits from the mssql-django backend.
    It overrides the sql_server_version property to fix a version detection bug.
    """

    @cached_property
    def sql_server_version(self):
        """
        Overrides the original buggy method.
        Instead of trying to detect the version, we hardcode it to 16,
        which corresponds to SQL Server 2022.
        """
        # Hardcoding the version to 16 (SQL Server 2022)
        return 16
