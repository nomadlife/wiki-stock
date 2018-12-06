import textwrap

from testproject.settings import base
# from django.conf import settings
import os
from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.staticfiles.templatetags.staticfiles import static

import pandas as pd
import pandas_datareader.data as web
from datetime import datetime,date
import matplotlib.pyplot as plt

from django.shortcuts import render
from django.views.generic import View

# Create your views here.
def test(request):
    return render(request, 'stock/test.html')

def home(request):
    return render(request, 'stock/home.html')

def stock_list(request):
    file = open(os.path.join(base.BASE_DIR, 'stock/statics/stock/kospi2.txt'))
    context = {'file_content': file.readlines(), 'name':'stock_list'}
    file.close()
    return render(request, 'stock/stock_list.html', context)

def stock_list2(request):
    file = open(os.path.join(base.BASE_DIR, 'stock/statics/stock/kospi2.txt'))
    data = [i.split('\t') for i in file.readlines()]
    context = {'file_content': data, 'name':'stock_list2'}
    file.close()
    return render(request, 'stock/stock_list.html', context)

def stock_list3(request):
    file = open(os.path.join(base.BASE_DIR, 'stock/statics/stock/alltickers_2018.csv'))
    data = [i.split(',') for i in file.readlines()]
    for j in data:
        j[2] = j[2].zfill(6)
    context = {'file_content': data, 'name':'stock_list3'}
    file.close()
    return render(request, 'stock/stock_list.html', context)

def stock_list_page(request):
    file = open(os.path.join(base.BASE_DIR, 'stock/statics/stock/alltickers_2018.csv'))
    data = [i.split(',') for i in file.readlines()]
    for j in data:
        j[2] = j[2].zfill(6)
    paginator = Paginator(data, 50)
    page = request.GET.get('page')
    data_paged = paginator.get_page(page)
    context = {'file_content': data_paged, 'name':'stock_list4_page' }
    file.close()
    return render(request, 'stock/stock_list_page2.html', context)

def stock_list_page2(request):
    file = open(os.path.join(base.BASE_DIR, 'stock/statics/stock/alltickers_2018.csv'))
    data = [i.split(',') for i in file.readlines()]
    for j in data:
        j[2] = j[2].zfill(6)
    paginator = Paginator(data, 50)
    page = request.GET.get('page')
    data_paged = paginator.get_page(page)
    context = {'file_content': data_paged, 'name':'stock_list5_page' }
    file.close()
    return render(request, 'stock/stock_list_page3.html', context)

def stock_search_list(request):
    if request.GET and request.GET['q'] != '':
        keyword = request.GET['q'].upper()
        file = open(os.path.join(base.BASE_DIR, 'stock/statics/stock/alltickers_2018.csv'))
        data = [i.split(',') for i in file.readlines()]
        for j in data:
            j[2] = j[2].zfill(6)
        data2 = [i for i in data if keyword in i[2] or keyword in i[1]]

        paginator = Paginator(data2, 50)
        page = request.GET.get('page')
        data_paged = paginator.get_page(page)

        context = {'file_content': data_paged , 'keyword':keyword}
        return render(request, 'stock/stock_list_page3.html', context)
    else:
        return redirect('stock-home')


## CBV 

class StockListPage(View):
    #hold
    file = open(os.path.join(base.BASE_DIR, 'stock/statics/stock/alltickers_2018.csv'))
    data = [i.split(',') for i in file.readlines()]
    for j in data:
        j[2] = j[2].zfill(6)
    template_name = 'stock/stock_list_page_cbv.html'
    context_object_name = {'file_content': data}
    paginate_by = 5

class StockListPage2(View):
    #hold
    template_name = 'stock/stock_list_page_cbv.html'
    context_object_name = 'posts'
    paginate_by = 5


def test_search(request, ticker_id):
    file = open(os.path.join(base.BASE_DIR, 'stock/statics/stock/alltickers_2018.csv'))
    data = [i.split(',') for i in file.readlines()]
    info = []
    for j in data:
        if j[0] == ticker_id:
            info = j
    today = date.today()
    start = datetime(2018, 11, 1)
    end = datetime(today.year, today.month, today.day)
    history_data = web.DataReader(info[2].zfill(6)+'.KS','yahoo',start, end)
    # history_data_new = history_data.sort_index(inplace=True, ascending=False)
    context = {'ticker_code':info[2].zfill(6), 'data':info, 'history_data':history_data}
    return render(request, 'stock/test_search.html', context )

def stock_detail(request, ticker_id):
    file = open(os.path.join(base.BASE_DIR, 'stock/statics/stock/alltickers_2018.csv'))
    data = [i.split(',') for i in file.readlines()]
    info = []
    for j in data:
        if j[0] == ticker_id:
            info = j
    ticker = info[2].zfill(6)+'.KS'
    today = date.today()
    end = datetime(today.year, today.month, today.day)
    start = datetime(today.year-1, today.month, today.day)
    history = web.DataReader(ticker,'yahoo',start, end)
    fig = plt.figure()
    history['Close'].plot(figsize=(10,6), grid=True, label='Close')
    fig.savefig(os.path.join(base.BASE_DIR, 'stock/statics/stock/chart/'+ticker+'.png'))
    fig = plt.figure()
    ax1 = plt.axes()
    ax1.xaxis.set_visible(False)
    ax1.set_yticklabels([])
    history['Close'].plot(figsize=(2,1), grid=False, label='Close')
    fig.savefig(os.path.join(base.BASE_DIR, 'stock/statics/stock/chart/'+ticker+'.m.png'))
    context = {'ticker_code':info[2].zfill(6), 'data':info , 'ticker':ticker}
    return render(request, 'stock/stock_detail.html', context )

def stock_detail2(request, ticker_id):
    print(ticker_id)
    file = open(os.path.join(base.BASE_DIR, 'stock/statics/stock/alltickers_2018.csv'))
    data = [i.split(',') for i in file.readlines()]
    info = []
    for j in data:
        if j[0] == ticker_id:
            info = j
    ticker = info[2].zfill(6)+'.KS'
    
    context = {'ticker_code':info[2].zfill(6), 'data':info , 'ticker':ticker, "customers":100}
    return render(request, 'stock/stock_detail.html', context )

def stock_detail3(request, ticker_id):
    file = open(os.path.join(base.BASE_DIR, 'stock/statics/stock/alltickers_2018.csv'))
    data = [i.split(',') for i in file.readlines()]
    info = []
    for j in data:
        if j[0] == ticker_id:
            info = j
    ticker = info[2].zfill(6)
    
    context = {'data':info , 'ticker':ticker, "customers":100}
    return render(request, 'stock/stock_detail.html', context )


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
# import random
# import string

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None,  *args, **kwargs):
        ticker = self.kwargs['ticker']
        df = pd.read_pickle(os.path.join(base.BASE_DIR, 'stock/statics/stock/data/{}'.format(ticker)))
        labels = df.index.strftime('%Y-%m-%d').tolist()
        values = df.Close.tolist()
        content = {
        "labels":labels,
        "values":values,
        }
        return Response(content)


def hello_fn(request, name="World"):
    return HttpResponse("Hello {}!".format(name))

class HomePageView(View):

    def dispatch(request, *args, **kwargs):
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Greetings to the world</title>
            </head>
            <body>
                <h1>Greetings to the world</h1>
                <p>Hello, world!</p>
            </body>
            </html>
        ''')
        return HttpResponse(response_text)