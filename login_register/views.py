from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from members.models import Photos
# Create your views here.

# Logic to register


def register_View(request):
    print(request.POST)
    if request.method == 'POST':
        first_name = request.POST['first_name'].strip()
        last_name = request.POST['last_name'].strip()
        username = request.POST['username'].strip()
        password1 = request.POST['password1'].strip()
        password2 = request.POST['password2'].strip()
        email = request.POST['email'].strip()

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print("username taken")
            elif User.objects.filter(email=email).exists():
                print("email taken")
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('user created')
                return redirect("login")
        else:
            print('password not matching....')

    return render(request, 'register.html', {})

# Logic to login


def login_View(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if(request.GET.get('next', '') == ''):
                print("user log in successfull")
                return redirect("members")
            else:
                return redirect(request.GET['next'])
        else:
            return HttpResponse("wrong value")
    else:
        return render(request, 'login.html', {})


# Logic to Logout


def logout_View(request):
    auth.logout(request)
    return redirect("explore")

# Deleting user uploads


def delete_useruploads(request):
    if request.method == "POST":
        user_post = Photos.objects.get(pk=request.POST['id'])
        user_post.delete()
        return redirect('members')
    else:
        return redirect('explore')
