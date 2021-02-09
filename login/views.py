from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import auth,User
from django.contrib import messages
from .models import userAccount

# view method to root request
def loginView(req):
    # return homepage 
    if req.method=='GET':
        return render(req,'appviews/login.html')
    # verify credentials
    elif req.method=='POST':
        username=req.POST['username']
        password=req.POST['password']
        
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(req,user)
            userprofile=userAccount.objects.filter(id=user.id)[0]
            user.up=userprofile
            return render(req,'appviews/home.html')
        else :
            return messages.error(req,"Invalid Credentials,Check Username or password")