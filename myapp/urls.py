from django.conf.urls import url
from myapp.views import *

urlpatterns = [
    url(r'^data/$', DataView.as_view(), name='login'),
    url(r'^auto/$', SearchView.as_view(), name='search'),
]
