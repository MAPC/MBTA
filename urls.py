from django.conf.urls.defaults import patterns, include, url
from django.views.generic.base import RedirectView



# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ('^$', RedirectView.as_view(url='/budgetcalculator/')),
    url(r'^budgetcalculator/', 'mbta.budgetcalc.views.index', name='budgetcalc-index'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Grappelli Admin Interface
    (r'^grappelli/', include('grappelli.urls')),
)
