from django.core.management.base import BaseCommand
from django.db import connection
import os
# python manage.py import_sql /path/to/your/file.ngr_sql


class Command(BaseCommand):
    help = 'Import SQL from file into PostgreSQL database'

    def add_arguments(self, parser):
        """
        Adds command line arguments to the parser.

        :param parser: Django's argparse parser
        """
        parser.add_argument('sql_file', type=str, help='Path to SQL file to import')

    def handle(self, *args, **kwargs):
        """
        Handle the command.

        :param args: list of positional arguments (not used)
        :param kwargs: dictionary of keyword arguments
        :return: None
        """
        sql_file = kwargs['sql_file']
        # Convert relative path to absolute path
        sql_file_path = os.path.abspath(sql_file)

        with open(sql_file_path, 'r') as f:
            sql_statements = f.readlines()
            print(len(sql_statements))

        with connection.cursor() as cursor:
            for statement in sql_statements:
                try:
                    cursor.execute(statement)
                    self.stdout.write(self.style.SUCCESS(f'Successfully executed SQL: {statement.strip()}'))
                except Exception as e:
                    self.stdout.write(self.style.WARNING(f'Data already exists in the database. Skipping insert: {statement.strip()}'))