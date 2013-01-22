from duplicate_proxy_model_test.one.models import One

class Report(One):
    
    class Meta:
        proxy = True
        app_label = 'duplicate_proxy_model_test.one'
    