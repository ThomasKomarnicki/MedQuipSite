from django.conf.urls import patterns, url
from django.http import HttpResponse

from Products import views

urlpatterns = patterns('',
    url(r'^(?P<product_sku>\d+)/$', views.product, name='product'),
    url(r'^Category/(?P<category_id>\d+)/$', views.category, name='category'),
    
)

