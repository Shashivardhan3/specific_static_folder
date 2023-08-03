from django.shortcuts import render

# Create your views here.


def specific_static(request):
    return render (request,'specific_static.html')


def specific_url_map(request):
    return render (request,'specific_url_map.html')