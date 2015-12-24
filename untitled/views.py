from django.http import HttpResponse,Http404,HttpRequest
import datetime
# from django.template import Template, Context
# from django.template.loader import get_template
from django.template import RequestContext
from django.template import TemplateDoesNotExist
from django.views.generic.base import TemplateView



from django.shortcuts import render
from books.models import Book

def custom_prc(request):
    return {'ip_adress': request.META['REMOTE_ADDR']}


def hello(request):
    return render(request,'hello.html')

def current_datetime(request):
    now = datetime.datetime.now()

    return render(request, 'current_datetime.html', {'current_date': now},
                  context_instance=RequestContext(request))

def hours_ahead(request,offset):
    try:
      ua = request.path

    except KeyError:
         ua = 'unknown'
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    #assert False
    return render(request, 'hours_ahead.html', {'hour_offset': offset, 'next_time': dt, 'brr': ua})

def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
             errors.append('Put the search request')
        elif len(q) > 20:
             errors.append('less then 20 symbols')
        else:
             books = Book.objects.filter(title__icontains=q)
             return render(request, 'search_form.html', {'books': books, 'query': q})

    return render(request, 'search_form.html', {'errors': errors})












