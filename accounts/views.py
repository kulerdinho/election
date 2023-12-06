from django.shortcuts import render, redirect

# Create your views here.


def Login_page(request):
    return render(request, 'pages/accounts/login_page.html')

def Forget_page(request):
    return render(request, 'pages/accounts/forget_page.html')

def Register_page(request):
    return render(request, 'pages/accounts/register_page.html')

def Logout_page(request):
    return redirect('login_page')
    
