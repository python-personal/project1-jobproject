from django.shortcuts import render

# Create your views here.
def homeview(request):
    return render(request,'testapp/home.html')

def ageview(request):
    uname=request.GET['uname']
    response=render(request,'testapp/age.html',{'uname':uname})
    response.set_cookie('uname',uname)
    return response

def gfview(request):
    uname=request.COOKIES['uname']
    age=request.GET['age']
    response=render(request,'testapp/gf.html',{'uname':uname})
    response.set_cookie('age',age)
    return response

def finalview(request):
    uname=request.COOKIES['name']
    age=request.COOKIES['age']
    gfname=request.GET['gfname']
    mydict={'uname':uname,'age':age,'gfname':gfname}
    return render(request,'testapp/final.html',mydict)
