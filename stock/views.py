import textwrap

from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render


# Create your views here.
def hello_fn(request, name="World"):
    return HttpResponse("Hello {}!".format(name))

def base(request, name="World"):
    return render(request, 'dir.html')

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