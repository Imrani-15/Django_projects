from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from authapp.forms import SignupForm
# Create your views here.
def home_page(request):
    return render(request,'authapp/home.html')

@login_required
def english_page(request):
    return render(request,'authapp/english.html')
@login_required
def hindi_page(request):
    return render(request,'authapp/hindi.html')
@login_required
def telugu_page(request):
    return render(request,'authapp/telugu.html')

def logout_page(request):
    return render(request,'authapp/logout.html')

def signup_page(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'authapp/signup.html',{'form':form})
