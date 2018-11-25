from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='stock-home'),
    url(r'^hello/$', views.hello_fn, name='stock-hello'),
    url(r'^base/$', views.base, name='stock-base'),

]