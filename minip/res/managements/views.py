from django.db.models import Count
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.utils.dateparse import parse_date
from django.core.files.storage import FileSystemStorage
import time
# Create your views here.

from classes.models import Restaurant, Faculty
def my_login(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user: 
            login(request, user)

            next_url = request.POST.get('next_url')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('index')
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'Wrong username or password!'

    next_url = request.GET.get('next')
    if next_url:
        context['next_url'] = next_url
    return render(request, template_name='login.html', context=context)


def my_logout(request):
    logout(request)
    return redirect('login')

@login_required
def res_add(request):
    msg = ''
    faculty_obj = Faculty.objects.all()
    print(faculty_obj)

    if request.method == 'POST':
        # print("aaaaaaaaaaaaaaaaaaaaaaaaaa")
        # print(ans)
        # print("aaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        faculty_id = request.POST.get('faculty')
        # myfile = request.FILES['picture']
        # fs = FileSystemStorage()
        test = request.POST.get('picture')
        print(test)
        res = Restaurant.objects.create(
            name = request.POST.get('name'),
            owner = request.POST.get('owner'),
            picture = request.POST.get('picture'),
            open_time = request.POST.get('open_time'),
            close_time = request.POST.get('close_time'),
            rating = int(request.POST.get('rating')),
            approve_by = request.POST.get('approve_by'),
            faculty = Faculty.objects.get(pk=faculty_id)
            # approve_date = datetime.strptime(request.POST.get('approve_date'), '%Y-%m-%d')
            # approve_date = date_a.strftime("%Y-%m-%d") #โค๊ดแม่งเอ๋ออออออออออออออออออ
            # approve_date = time.strptime(request.POST.get('approve_date'), '%Y-%m-%d')
            # approve_date = time.mktime(datetime.strptime(request.POST.get('approve_date'), "%Y-%m-%d").date())
        )
        
        msg = 'Successfully create new Restaurant - username: %s' % (res.name)
        print(request.POST.get('name'), "created")
        redirect('index')
        
    else:
        res = Restaurant.objects.none()

    context = {
        'res': res,
        'msg': msg,
        'faculty': faculty_obj
    }

    return render(request, 'res_form.html', context=context)
