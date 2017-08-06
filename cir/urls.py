from django.conf.urls import url
from django.conf.urls.static import static

from cir import views
from cir.views import post_list
from cir1 import settings

urlpatterns = [
    url(r'^export/', views.export_data, name="export"),
    url(r'^post/', post_list, name='post'),
    url(r'^search_ctc', views.export_ctc, name="ctc"),
    url(r'^search_company', views.export_company, name="company"),
    url(r'^search_branch', views.export_branch, name="branch"),
    url(r'^search_date', views.export_date, name="date"),
    url(r'^home', views.home, name="home"),
]

