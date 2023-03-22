from django.shortcuts import render, redirect
# 로그인 정보를 입력할 때 필요한 폼가져오기
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# Create your views here.
def login(request):

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("articles:index")
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    form = AuthenticationForm()
    context = {"form" : form}
    auth_logout(request)
    # return redirect("articles:index")
    return render(request, "accounts/babo.html", context)
