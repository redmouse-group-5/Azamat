# coding=utf-8

from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views.decorators.cache import cache_page

from Student.form import LoginForm
from aboutPageIntent.models import HistoryOfNCKT, OurOrder, Vip
from firstDates.models import HeaderDate
from homePageIntent.models import HelloGrid, SpectrFach, MoreInformation
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from picture.models import GroupOfPicture, Picture
from Student.models import StudentInfo


# @cache_page(30, key_prefix="site1", cache="filecache")
def open_start_page(request):
    Date = get_object_or_404(HeaderDate)
    Grid = get_object_or_404(HelloGrid)
    fach_list = SpectrFach.objects.filter(publick=True).order_by('name')
    info_list = MoreInformation.objects.filter(publick=True)
    return render(request, 'index.html', {'date': Date, 'grid': Grid, 'fach_list': fach_list, 'info_list': info_list,
                                          'username': auth.get_user(request).username})


def open_about_pages(request):
    Date = get_object_or_404(HeaderDate)
    History_list = HistoryOfNCKT.objects.filter(publick=True).order_by('pk')
    Order_list = OurOrder.objects.filter(publick=True).order_by('pk')
    Person_list = Vip.objects.filter(publick=True).order_by('range')

    return render(request, 'about.html', {'date': Date, 'history_list': History_list, 'order_list': Order_list, 'person_list':Person_list,
                                          'username':auth.get_user(request).username})

def open_gallery_page(request):
    if auth.get_user(request).is_authenticated:
        args = {}
        args['date'] = get_object_or_404(HeaderDate)
        args['group'] = GroupOfPicture.objects.all()
        # args['picture'] = Picture.objects.get()
        args['username'] = auth.get_user(request).username
        return render(request, 'gallery.html', args)
    else:
        form = AuthenticationForm
        error = 'Чтобы войти в галерею, пожалуйста авторезируйтесь'
        return render(request, 'signin.html', {'login_error':error, 'form':form})



def redirect_to_start_page(request):
    return redirect('http://127.0.0.1:8000/index')

def open_map_page(request):
    args = {}
    Date = get_object_or_404(HeaderDate)
    args['date'] = Date
    username = auth.get_user(request).username
    args['username'] = username
    args['student_list'] = StudentInfo.objects.all()
    return render(request, 'map.html', args)
