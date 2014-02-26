from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^(\d+)/$', 'lists.views.view_list',name='view_list'),
    url(r'^(\d+)/new_item$','lists.views.add_item', name='add_item'),
    url(r'^new$', 'lists.views.new_lists',name='new_lists')
    ,
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),
)
