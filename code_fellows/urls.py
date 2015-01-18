from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
import challangeapp.views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', challangeapp.views.ListContactView.as_view(),
        name='contacts-list',),
    url(r'^new$', challangeapp.views.CreateContactView.as_view(),
    name='contacts-new',),
    url(r'^edit/(?P<pk>\d+)/$', challangeapp.views.UpdateContactView.as_view(),
        name='contacts-edit',),
    url(r'^delete/(?P<pk>\d+)/$', challangeapp.views.DeleteContactView.as_view(),
        name='contacts-delete',),
    url(r'^(?P<pk>\d+)/$', challangeapp.views.ContactView.as_view(),
        name='contacts-view',),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()