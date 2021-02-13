from django.contrib import auth,messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from . models import pendingitems

# Create your views here.
from django.shortcuts import render,HttpResponse
from . models import book,ordereditems
# Create your views here.
data = book.objects.all()
def home(request):
    if request.user.is_authenticated:
         return render(request,'home2.html' ,{'data':data})
    else:
         return render(request, 'home.html', {'data': data})
def order(request):
    if request.method=="POST":
        bookname1=request.POST['bookname1']
        quantity=request.POST['quantity']
        price=request.POST['price']
        if bookname1 and quantity:
            username=request.user.username
            x=ordereditems(bookname1=bookname1,username=username,quantity=quantity,price=price)
            x.save()
            messages.success(request,"Added to Cart sucessfully")
            return render(request,'home2.html',{'data':data})
        else :
            return  HttpResponse("enter all fields")
def signupform(request):
    return render(request,'signupform.html')
def register(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if cpassword==password:
            if username and password:
                x=User.objects.create_user(username=username,password=password)
                x.save()
                return render(request,'confirmation.html')
            else:
                return HttpResponse("enter all fields")
        else:
            return HttpResponse("passwords didnt match")
def loginform(request):
    return render(request,'loginform.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'home2.html',{'data':data})
def cart(request):
    dat=ordereditems.objects.filter(username=request.user.username)
    ca=0
    for i in dat:
        ca=ca+int(i.quantity)*int(i.price)

    return render (request,'cart.html',{'dat':dat,'ca':ca})
def logout(request):
    auth.logout(request)
    return redirect('/')
def search(request):

    if request.user.is_authenticated:
        searc=request.POST['search']
        dat = book.objects.all()
        l=[]
        for i in dat:
            l.append(i.bookname)
        if searc in l:
                dat = book.objects.filter(bookname=searc)
                for i in dat:
                   if searc==i.bookname:
                     bo=i.bookname
                     bo1=i.price
                     bo2=i.image
                     return render(request,'home3.html',{'bo':bo,'bo1':bo1,'bo2':bo2})
        else :
                  no="Not found"
                  return render(request,'home4.html',{'no':no})
    else:
        searc = request.POST['search']
        dat = book.objects.all()
        l = []
        for i in dat:
            l.append(i.bookname)
        if searc in l:
            dat = book.objects.filter(bookname=searc)
            for i in dat:
                if searc == i.bookname:
                    bo = i.bookname
                    bo1 = i.price
                    bo2 = i.image
                    return render(request, 'home5.html', {'bo': bo, 'bo1': bo1, 'bo2': bo2})
        else:
            no = "Not found"
            return render(request, 'home4.html', {'no': no})
l2=[]
def confirm(request):
    if request.method=="POST":
        bookname1=request.POST['bookname1']
        quantity=request.POST['quantity']
        price=request.POST['price']
        username=request.user.username
        dat=pendingitems.objects.filter(username=request.user.username)


        if bookname1 not in l2:
            l2.append(bookname1)
            x1 = pendingitems(bookname1=bookname1, username=username, quantity=quantity, price=price)
            x1.save()
            messages.success(request,"order confirmed")
            return redirect('cart')
        else:
            messages.success(request, "order already confirmed")
            return redirect('cart')


def cart2(request):
    dat = pendingitems.objects.filter(username=request.user.username)
    ca = 0
    for i in dat:
        ca = ca + int(i.quantity) * int(i.price)
    return render(request,'cart2.html',{'dat': dat, 'ca': ca})


