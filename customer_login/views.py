from django.shortcuts import render,redirect,HttpResponseRedirect,reverse
from django.contrib.auth.models import User,auth
from  django.contrib import messages
from .models import CustomerProfile, Contact


def login(request):

    if request.method == 'POST':

            name = request.POST['name']
            password = request.POST['password']

            user = auth.authenticate(username=name,password=password)

            if user is not None:
                auth.login(request,user)
                return HttpResponseRedirect(reverse('shop:ShopHome'))
            else:
                messages.error(request,'Invalid Credientials, Please Try Again! ')
                return redirect('login')
            
    else:
        return render(request,'login.html')

def register(request):
    
    if request.method == 'POST':
        
        name=request.POST['name']
        password = request.POST['password']
        repassword = request.POST['repassword']
        contact = request.POST['contact']
        email = request.POST['email']
        gender=request.POST['gender']

        if password == repassword :
            if User.objects.filter(username=name).exists():
                messages.error(request,'Username Already Exist!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'Email Already Exists!')
                return redirect('register')
            else:
                user=User.objects.create_user(username=name,password=password,email=email,first_name=name)
                user.save()
                customerprofile=CustomerProfile(user = User.objects.get(username=name),contact=contact,gender=gender)
                customerprofile.save()
                messages.success(request, 'Your Account is Successfully Created')
                return HttpResponseRedirect(reverse('login'))
        else:
            messages.error(request, 'Confirm Your Password Once Again!!!')
            return redirect('register')
       
    else :
        return render(request,'register.html')
        

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        messages.success(request, "Your Message has been Sent!!")
        contact.save()
    return render(request, 'contact.html')



