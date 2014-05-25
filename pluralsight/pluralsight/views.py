from django.views.generic.base import View
from django.shortcuts import render_to_response
from datetime import date
#from django.http import HttpResponse

class HelloWorldView(View):
  def get(self, request):
    return render_to_response('helloworld.html', {'date': date.today()})
    #return HttpResponse("Hello, World!");
