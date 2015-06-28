from django.conf.urls import include, url
from django.contrib import admin

from herokudemo import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.MyView.as_view(), name='home'),
]
