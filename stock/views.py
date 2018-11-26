import textwrap

from testproject.settings import base
# from django.conf import settings
import os
from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render


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