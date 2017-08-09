from django.conf.urls import url
from django.conf.urls.static import static


from StudentLogin import views
from cir1 import settings
from StudentLogin.views import CompanyList


urlpatterns = [
    url(r'^home/$', views.home, name="home"),
    url(r'^display/$', CompanyList.as_view()),
]
