from django.conf.urls import patterns, include, url

# from django.contrib import admin

from views import *


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', loginView),
    url(r'^dashboard$', dashboardView),
    url(r'^users/stats$', usersView),
    url(r'^users/list$', usersListView),
    url(r'^items/stats$', itemsView),
    url(r'^items/list$', itemsListView),
    url(r'^logout$', logoutView)
)
