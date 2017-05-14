from django.conf.urls import url
from . import views

app_name = 'loop'

urlpatterns = [

    # /loop/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /loop/<company_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # /loop/company/add/
    url(r'^company/add/$', views.CompanyCreate.as_view(), name='company-add'),
    # /loop/company/1/
    url(r'^company/(?P<pk>[0-9]+)/$', views.CompanyUpdate.as_view(), name='company-update'),
    # /loop/company/1/delete/
    url(r'^company/(?P<pk>[0-9]+)/delete/$', views.CompanyDelete.as_view(), name='company-delete'),
]
