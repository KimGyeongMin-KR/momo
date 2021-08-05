from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import MomoUser
from .forms import LoginForm
# Create your views here.

def home(request):
    user_id = request.session.get('user')
    if user_id :
        Momouser = MomoUser.objects.get(pk = user_id)
        return HttpResponse(Momouser.username)
    return HttpResponse('Home!')

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')


def login(request):
    if request.method == 'GET':
        return render(request, 'html/login.html')
    elif request.method == 'POST':
        username = request.POST.get('userName', None)
        password = request.POST.get('password', None)

        res_data = {}
        if not (username and password):
            res_data ['error'] ='모든 값을 입력해야합니다'
        else:
            Momouser = MomoUser.objects.get(username=username)
            if check_password(password, Momouser.password):
                request.session['user'] = Momouser.id
                return redirect('/')
            else:
                res_data['error'] = '아이디 또는 비밀번호를 확인해주세요'

        return render(request, 'html/login.html', res_data)


def register(request):
    if request.method == 'GET':
        return render(request, 'html/register.html')
    elif request.method == 'POST':
        username = request.POST.get('userName', None)
        password = request.POST.get('password', None)
        passwordChk = request.POST.get('passwordChk', None)
        email = request.POST.get('email', None)


        res_data = {}

        if not (username and password and passwordChk and email):
            res_data['error'] = '모든 값을 입력해야합니다.'
        elif password != passwordChk:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            momouser = MomoUser(
                username = username,
                password = make_password(password),
                useremail = email
            )

            momouser.save()

        return render(request, 'html/register.html', res_data)
