from django.conf.urls import url
from django.views.generic.base import RedirectView
from . import views

favicon_view = RedirectView.as_view(url='/static/images/favicon.png', permanent=True)

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
	url(r'^favicon\.ico$', favicon_view),
]
