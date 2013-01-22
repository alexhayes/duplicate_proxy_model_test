from duplicate_proxy_model_test.two.models import Two

class Report(Two):
    
    class Meta:
        proxy = True
        app_label = 'duplicate_proxy_model_test.two'
    