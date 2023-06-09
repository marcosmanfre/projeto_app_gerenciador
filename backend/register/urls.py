from register import views

from django.urls import re_path as url

from django.conf import settings

urlpatterns=[
    url(r'^employee$',views.employeeApi),
    url(r'^employee/([0-9]+)$',views.employeeApi),


        
    url(r'pessoa$',views.pessoaApi),
    url(r'pessoa/([0-9]+)$',views.pessoaApi),

    
]