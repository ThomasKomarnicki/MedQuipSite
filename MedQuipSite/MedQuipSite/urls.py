from django.conf.urls import patterns, include, url
from django.contrib import admin
import views
from Customers import views as customer_views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^$', views.home, name='home'),
    url(r'^AboutUs', views.about_us, name='about'),
    url(r'^ContactUs', views.contact_us, name='contact'),
    url(r'^Products/', include('Products.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(myAccount/)',include('Customers.urls')),
    url(r'^Cart',views.my_cart),
    url(r'^Search/',views.search),
    url(r'^Register/',customer_views.register),
    url(r'^Thanks/',customer_views.register_thanks),  
)