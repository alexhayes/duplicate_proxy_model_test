Using django@master it appears that proxy models can't share the same name.

# Install

```bash
git clone git://github.com/alexhayes/duplicate_proxy_model_test.git
cd duplicate_proxy_model_test
./manage.py syncdb
```

# Example

```python
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
```

I would have expected to get the following output:

```bash
<class 'duplicate_proxy_model_test.one.reports.foo.Report'>
<class 'duplicate_proxy_model_test.two.reports.bar.Report'>
```

However what is actually output is:

```bash
<class 'duplicate_proxy_model_test.one.reports.foo.Report'>
<class 'duplicate_proxy_model_test.one.reports.foo.Report'>
```

This management command can be run with the following:

```bash
./manage.py test_duplicate_names
```