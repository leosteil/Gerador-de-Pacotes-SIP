from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.index),

    url(r'^cadastro/$', views.cadastro),
    url(r'^login/$', views.login),
    url(r'^newSIP/$', views.newSip),
    url(r'^empacotar/$', views.empacotar),

]
