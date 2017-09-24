from django.conf.urls import url
from django.conf.urls.static import static
from faculty import views
from faculty.views import StudentList

urlpatterns = [
    url(r'^home/$', views.home, name="home"),
    url(r'^students/$', StudentList.as_view()),
    url(r'^upload/(?P<pk>\d+)/$', views.upload, name="upload"),
]
