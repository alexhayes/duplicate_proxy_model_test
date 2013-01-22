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

# THE FIX!!!

Thanks to charettes and akaariai the solution is to [define app_label](https://docs.djangoproject.com/en/dev/ref/models/options/#app-label) 
on your model.

See [this commit](https://github.com/alexhayes/duplicate_proxy_model_test/commit/82803c6e41d6e8369c4e93859c20f12d3b834659)
for an example of how this can be done.

