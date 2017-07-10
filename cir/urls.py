from django.conf.urls import url

from cir import views
from cir.views import post_list

urlpatterns = [
    url(r'^export/', views.export_data, name="export"),
    url(r'^post/(?P<ak>[0-9]+)/', post_list, name='post'),
]

