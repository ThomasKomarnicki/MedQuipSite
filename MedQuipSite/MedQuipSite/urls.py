from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^AboutUs', views.about_us, name='about'),
    url(r'^ContactUs', views.contact_us, name='contact'),
    url(r'^Products/', include('Products.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(myAccount/)|(Register)',include('Customers.urls'))
)