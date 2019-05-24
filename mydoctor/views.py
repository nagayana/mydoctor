from django.http import HttpResponse
from django .template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import UserForm
from django.shortcuts import render, get_object_or_404, redirect


def home(request):
    return render(request,"apnadoctor1/home.html")

# def first_login(request):
#     form = UserForm(request.POST or None)
#     context = {
#         "form": form,
#     }
#     return render(request, 'apnadoctor1/login.html', context)


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'apnadoctor1/home.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("mydoctor:index")
            else:
                return render(request, 'apnadoctor1/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'apnadoctor1/login.html', {'error_message': 'Invalid login'})
    return render(request, 'apnadoctor1/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'apnadoctor1/index.html')
    context = {
        "form": form,
    }
    return render(request, 'apnadoctor1/register.html', context)



def index(request):
    if not request.user.is_authenticated():
        return redirect("mydoctor:login_user")
    return render(request, 'apnadoctor1/index.html')


def test_result(request):
    if request.method == "POST":
        content=request.POST['content']
        return render(request,'apnadoctor1/result.html',{'content':content})
    else:
        return redirect("apnadoctor1:login_user")
