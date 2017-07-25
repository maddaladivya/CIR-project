from django.conf.urls import url

from cir import views
from cir.views import post_list

urlpatterns = [
    url(r'^export/', views.export_data, name="export"),
    url(r'^post/', post_list, name='post'),
    url(r'^exp/', views.export_data_query, name="query"),
    url(r'^$', views.home, name="home"),
]

