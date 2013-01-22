from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        """
        Clean various records in the CodeIgniter database.
        """
        from duplicate_proxy_model_test.one.reports.foo import Report as FooReport
        from duplicate_proxy_model_test.two.reports.bar import Report as BarReport
        print FooReport
        print BarReport