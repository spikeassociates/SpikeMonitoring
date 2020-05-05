from django.conf import settings


def global_settings(request):
    return {
        'ENABLE_SUBSCRIPTION': settings.ENABLE_SUBSCRIPTION,
        'ENABLE_DUTY_ROTA': settings.ENABLE_DUTY_ROTA,
        'LOGO48' : 'arachnys/img/logo_48x48.png',
        'COMPANY_NAME' : 'Spike Monitoring',
        'ENABLE_MANUAL_REPORTING': settings.ENABLE_MANUAL_REPORTING,
    }
