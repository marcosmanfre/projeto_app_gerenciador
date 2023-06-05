from register import views
from django.urls import re_path as url
from django.conf import settings

urlpatterns=[

    url(r'pessoa$',views.pessoaApi),
    url(r'pessoa/([0-9]+)$',views.pessoaApi),

]