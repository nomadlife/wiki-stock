from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='stock-home'),
    url(r'^hello/$', views.hello_fn),

    url(r'^cbvtest/$', views.HomePageView.as_view()),

    url(r'^list/$', views.stock_list),
    url(r'^list2/$', views.stock_list2),
    url(r'^list3/$', views.stock_list3),
    url(r'^list4/$', views.stock_list_page),
    url(r'^list5/$', views.stock_list_page2, name='stock-list'),

    url(r'^search/$', views.stock_search_list, name='stock-search'),

    url(r'^list5/$', views.StockListPage.as_view()),
    url(r'^list6/$', views.StockListPage2.as_view()),

    url(r'^detail/(?P<ticker_id>.+?)/', views.test_search),
    url(r'^detail2/(?P<ticker_id>.+?)/', views.stock_detail),
    url(r'^detail3/(?P<ticker_id>.+?)/', views.stock_detail2),
    url(r'^detail4/(?P<ticker_id>.+?)/', views.stock_detail3, name='ticker-detail'),

    url(r'^api/chart/data/(?P<ticker>.+?)/', views.ChartData.as_view()),
    url(r'^api/chart/data2/(?P<ticker>.+?)/', views.ChartData2.as_view(), name='api-chart-data'),

]