from urllib import request

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Mobile
from .forms import MobileForm


# Create your views here.
# def demo(request):
#   return HttpResponse("Hello world..!!")
def demo(request):
    obj = Mobile.objects.all()
    context = {
        'mobile_list': obj
    }
    return render(request, 'index1.html', context)
    # return render(request,'index.html',{'result':obj})


def details(request, mobile_id):
    mobile = Mobile.objects.get(id=mobile_id)
    return render(request, "detail.html", {'mobile': mobile})


def add_mobile(request):
    if request.method == "POST":
        name = request.POST.get('name', )
        desc = request.POST.get('desc', )
        year = request.POST.get('year', )
        img = request.FILES['img']
        mobile = Mobile(name=name, desc=desc, year=year, img=img)
        mobile.save()
    return render(request, 'add.html')


def edit_mobile(request, id):
    mobile = Mobile.objects.get(id=id)
    form = MobileForm(request.POST or None, request.FILES, instance=mobile)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'editform.html', {'form': form, 'mobile': mobile})
def delete(request, id):
    if request.method == "POST":
        mobile = Mobile.objects.get(id=id)
        mobile.delete()
        return redirect('/')
    return render(request,'delete.html')