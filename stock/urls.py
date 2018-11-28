from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='stock-hello'),
    url(r'^hello/$', views.hello_fn),

    url(r'^cbvtest/$', views.HomePageView.as_view()),

    url(r'^list/$', views.stock_list),
    url(r'^list2/$', views.stock_list2),
    url(r'^list3/$', views.stock_list3),
    url(r'^list4/$', views.stock_list_page, name='stock-home'),

    url(r'^list5/$', views.StockListPage.as_view()),
    url(r'^list6/$', views.StockListPage2.as_view()),

    url(r'^search/(?P<ticker_id>.+?)/', views.test_search),
    url(r'^search2/(?P<ticker_id>.+?)/', views.stock_detail, name='ticker-search'),

]