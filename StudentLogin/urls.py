from django.conf.urls import url, include
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from StudentLogin import views
from cir1 import settings
from django.contrib.auth import views as auth_views
from StudentLogin.views import CompanyList, ProfileDetailView

urlpatterns = [
    url(r'^home/$', views.home, name="home"),
    url(r'^display/$', CompanyList.as_view()),
    url(r'^register/$', views.register, name='register'),
    url(r'^info/(?P<pk>[0-9]+)/$', views.info, name="info"),
    url(r'^login/$', auth_views.login, {'template_name': 'StudentLogin/login.html'}, name='login'),
    url('^', include('django.contrib.auth.urls')),
    url(r'^index/$', views.index, name='index'),
    url(r'^(?P<pk>\d+)/$', ProfileDetailView.as_view(), name="profile"),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^logout/$', auth_views.logout, name="logout"),
]
