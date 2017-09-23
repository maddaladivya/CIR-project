from django.conf.urls import url
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from StudentLogin import views
from cir1 import settings
from django.contrib.auth.views import logout
from StudentLogin.views import CompanyList

urlpatterns = [
    url(r'^home/$', views.home, name="home"),
    url(r'^display/$', CompanyList.as_view()),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', auth_views.login, {'template_name': 'StudentLogin/login.html'}, name='login'),
    url(r'^index/$', views.index, name='index'),
    url(r'^logout/$', logout,
                          {'next_page': '/student/home/'}),
    url(r'^profile/(?P<ak>[0-9]+)/$', views.profile, name='profile'),

]
