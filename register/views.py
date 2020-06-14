from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
def register(request):

    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        pswd = request.POST['password']

        if User.objects.filter(username=username).exists():
            print('Username is taken')
        elif User.objects.filter(email=email).exists():
            print('Email is taken')
        else:
            user = User.objects.create_user(username=username, password=pswd, email=email)
            user.save()
            print('user created')
            return redirect("/")
    else:    
        return render(request, 'register/regpage.html') 