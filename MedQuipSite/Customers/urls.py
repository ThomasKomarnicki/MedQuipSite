from django.conf.urls import patterns, url
from django.http import HttpResponse

from Customers import views

urlpatterns = patterns('',
    url(r'^login/',views.login), 
    url(r'^myAccount/Orders/(?P<order_id>\d+)', views.order, name='orders'),
    url(r'^myAccount/Orders', views.orders, name='orders'),
    url(r'^myAccount/$', views.my_account, name='my_account'),
    
)

