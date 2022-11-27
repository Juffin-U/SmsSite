from django.urls import path

from .views import *

urlpatterns = [
    path('', index,name='sms'),
    path('api/sms', get_single_sms, name='sms_api')
]
