from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import *
from django.forms.models import model_to_dict


def test(request):
    return HttpResponse("hello world")
def search_list(request):
    resultObject = students.objects.all().order_by("cID")
    # for d in resultObject:
    #     print(model_to_dict(d))
    return render(request,"search_list.html",locals())

   
         


   



    return HttpResponse("hello world")
