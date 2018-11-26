from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='stock-list'),
    url(r'^hello/$', views.hello_fn, name='stock-hello'),
    url(r'^home2/$', views.HomePageView.as_view(), name='stock-home2'),
    url(r'^list/$', views.stock_list3, name='stock-home'),


]