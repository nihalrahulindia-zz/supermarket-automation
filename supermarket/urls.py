from django.conf.urls import url

from . import views

app_name = 'supermarket'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^print/$', views.print, name='print'),
    url(r'^update/$', views.update, name='update'),
    url(r'^see/$', views.see, name='see'),
    url(r'^change/$', views.change, name='change'),
    url(r'^statistics/$', views.statistics, name='statistics'),
]
