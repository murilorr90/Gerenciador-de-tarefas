from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dev01.views.home', name='home'),
    # url(r'^dev01/', include('dev01.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    url(r'^projects/$', 'dev01.gerenciadorprojetos.views.project_index'),    
    url(r'^projects/create/$', 'dev01.gerenciadorprojetos.views.project_create'),
    url(r'^projects/edit/(?P<project_id>\d+)/$', 'dev01.gerenciadorprojetos.views.project_edit'),
    url(r'^projects/update/(?P<project_id>\d+)/$', 'dev01.gerenciadorprojetos.views.project_update'),
    url(r'^projects/new/$', 'dev01.gerenciadorprojetos.views.project_new'),
    url(r'^projects/(?P<project_id>\d+)/$', 'dev01.gerenciadorprojetos.views.project_show'),
    #url(r'^/project/(?P\d+)/edit$', 'dev01.gerenciadorprojetos.views.project_edit'),

    #url(r'^tasks/$', 'dev01.gerenciadorprojetos.views.task_index'),    
    #url(r'^tasks/new/$', 'dev01.gerenciadorprojetos.views.task_new'),
    #url(r'^tasks/create/$', 'dev01.gerenciadorprojetos.views.task_create'),
    #url(r'^tasks/edit/(?P<project_id>\d+)/$', 'dev01.gerenciadorprojetos.views.task_edit'),
    #url(r'^tasks/update/(?P<project_id>\d+)/$', 'dev01.gerenciadorprojetos.views.task_update'),
    url(r'^projects/(?P<project_id>\d+)/tasks/$', 'dev01.gerenciadorprojetos.views.task_index'),  
    url(r'^projects/(?P<project_id>\d+)/tasks/new/$', 'dev01.gerenciadorprojetos.views.task_new'),
    url(r'^projects/(?P<project_id>\d+)/tasks/create/$', 'dev01.gerenciadorprojetos.views.task_create'),
    url(r'^projects/(?P<project_id>\d+)/tasks/(?P<task_id>\d+)/edit/$', 'dev01.gerenciadorprojetos.views.task_edit'),
    url(r'^projects/(?P<project_id>\d+)/tasks/(?P<task_id>\d+)/update/$', 'dev01.gerenciadorprojetos.views.task_update'),
)
