import textwrap

from testproject.settings import base
# from django.conf import settings
import os
from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.staticfiles.templatetags.staticfiles import static

import pandas as pd
import pandas_datareader.data as web
from datetime import datetime,date

# Create your views here.
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
    paginator = Paginator(data, 40)
    page = request.GET.get('page')
    data_paged = paginator.get_page(page)
    context = {'file_content': data_paged, 'name':'stock_list3_page' }
    file.close()
    return render(request, 'stock/stock_list_page.html', context)


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