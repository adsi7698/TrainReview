from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.index, name="index"),
    url(r'^Passengers/', include('Passengers.urls')),
]

urlpatterns += staticfiles_urlpatterns()