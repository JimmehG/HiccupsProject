from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^deadlines/$', views.deadlines, name='deadlines'),
	url(r'^waterfall/$', views.waterfall, name='waterfall'),
	url(r'^bliss/$', views.bliss, name='bliss'),
	url(r'^bourgeois/$', views.bourgeois, name='bourgeois'),
	url(r'^cigarette/$', views.cigarette, name='cigarette'),
	url(r'^spacecadet/$', views.spacecadet, name='spacecadet'),
	url(r'^complexion/$', views.complexion, name='complexion'),
	url(r'^noisecancelling/$', views.noisecancelling, name='noisecancelling'),
	url(r'^databug/$', views.databug, name='databug'),
	url(r'^$', views.index, name='index'),
]
