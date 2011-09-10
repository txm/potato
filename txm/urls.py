from django.conf.urls.defaults import *

urlpatterns = patterns('',
    #('^$', 'django.views.generic.simple.direct_to_template', {'template': 'home.html'}),

    ('^$', 'txm.views.blogs'),
    ('^blog/(\d+)$', 'txm.views.blog_view'),

    ('^admin/$', 'txm.views.admin_home'),
    ('^admin/edit/', 'txm.views.admin_edit'),
    ('^admin/delete/', 'txm.views.admin_delete'),
)


