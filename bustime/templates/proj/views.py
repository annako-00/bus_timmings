from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import *
from .models import *
from django.views.generic import ListView,DetailView,CreateView
from django.db.models import Q



def ba(request):
     return render(request,'base2.html')

def ahome(request):
     return render(request,'ahome2.html')

def AbusList(request):
     bus=Busprofile.objects.all()
     return render(request,'abuslist.html',{'bu':bus})

def aupnoti(request):
          noti=Updates.objects.all()
          return render(request,'aupdatenotif.html',{'n':noti})

def anotif(request):
     noti=Updates.objects.all()
     return render(request,'aviewnotif.html',{'n':noti})

def profile(request):
     u=User.objects.all()
     return render(request,'profile.html',{'u':u})


def aup(request,id):
     a1=User.objects.get(id=id)
     if request.method=='POST':
          f1=Regform(request.POST,instance=a1)
          if f1.is_valid():
               f1.save()
               return redirect(profile)
     else:
          f1=Regform(instance=a1)
     return render(request,'aedit.html',{'f':f1})

def adtl(request,id):
     d1=User.objects.get(id=id)
     if request.method=='POST':
          d1.delete()
          return redirect(profile)
     return render(request,'adelete.html',{'d1':d1})

def anoti(request):
     if request.method=='POST':
          form=Eform(request.POST)
          if form.is_valid():
               form.save()
               messages.success(request,'Updated')
               return redirect(aupnoti)
     else:
          form=Eform()
     return render(request,'aadnotif.html',{'o':form})

def back(request):
    return redirect(ahome)


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('passw1')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                 return redirect(ahome)
            messages.success(request, 'User has been logged in.')
            return redirect(ho)  
        else:
            user_obj = None 

            try:
                user_obj = User.objects.get(username=username)
            except User.DoesNotExist:
                pass 
            if user_obj and not user_obj.check_password(password):
                messages.error(request, 'Incorrect password for the provided username.')
            else:
                messages.error(request, 'Invalid login credentials.')

    return render(request, 'login.html')

def logoutpage(request):
     logout(request)
     messages.success(request,'user has been logged out')
     return redirect(ba)

def header(request):
     return render(request,'header.html')

def about(request):
     return render(request,'about.html')

def base(request):
     return render(request,'base.html')

def main(request):
     return render(request,'main.html')

def footer(request):
     return render(request,'footer.html')

def home(request):
     return render(request,'home.html')

def ho(request):
     return render(request,'home2.html')

def btime(request):
     return render(request,'bustimeadd.html')

def Reg(request):
     if request.method=='POST':
          form=Regform(request.POST)
          if form.is_valid():
               form.save()
               messages.success(request,'user registered')
               return redirect(ba)
     else:
          form=Regform()
     return render(request,'register.html',{'form':form})


def BusList(request):
     bus=Busprofile.objects.all()
     return render(request,'bustimesee.html',{'bu':bus})

def notif(request):
     noti=Updates.objects.all()
     return render(request,'viewnotif.html',{'n':noti})

class Createupdate(CreateView):
     model=Updates
     fields='__all__'
     context_object_name='form'
     template_name='bustimeadd.html'
     success_url='ho'

def go_back(request):
    return redirect(ba)

def goback(request):
    return redirect(ho)

def up(request,id):
     a1=Updates.objects.get(id=id)
     if request.method=='POST':
          form=Uproform(request.POST,instance=a1)
          if form.is_valid():
               form.save()
               return redirect('prof')
     else:
          form=Uproform(instance=a1)
     return render (request,'edit.html',{'form':form})


def noti(request):
     if request.method=='POST':
          form=Eform(request.POST)
          if form.is_valid():
               form.save()
               messages.success(request,'Updated')
               return redirect(upnoti)
     else:
          form=Eform()
     return render(request,'addnotif.html',{'o':form})

def upnoti(request):
          noti=Updates.objects.all()
          return render(request,'updatenotif.html',{'n':noti})

def search(request):
    query = request.GET.get('q')

    if query:
        results = Stopname.objects.filter(stopname__icontains=query).values('stoptime', 'stopname', 'brname__bname', 'routename__route')
    else:
        results = Stopname.objects.none()

    return render(request, 'searchresults.html', {'results': results, 'query': query})

def eedit(request,id):
     a1=Updates.objects.get(id=id)
     if request.method=='POST':
          f1=Eform(request.POST,instance=a1)
          if f1.is_valid():
               f1.save()
               return redirect(aupnoti)
     else:
          f1=Eform(instance=a1)
     return render(request,'edit.html',{'f1':f1})

def dtl(request,id):
     d1=Updates.objects.get(id=id)
     if request.method=='POST':
          d1.delete()
          return redirect(aupnoti)
     return render(request,'delete.html',{'d1':d1})