from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User, auth
from members.models import Photos
# Create your views here.

# Logic to register


def register_View(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        username = request.POST.get('username', '').strip()
        password1 = request.POST.get('password1', '').strip()
        password2 = request.POST.get('password2', '').strip()
        email = request.POST.get('email', '').strip()

        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')
        else:
            user = User.objects.create_user(
                username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
            user.save()
            messages.success(request, 'Registration successful! Please login.')
            return redirect("login")

    return render(request, 'register.html', {})

# Logic to login


def login_View(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        next_url = request.POST.get('next', '').strip() or request.GET.get('next', '').strip()

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if next_url:
                return redirect(next_url)
            return redirect("members")
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html', {})


# Logic to Logout


def logout_View(request):
    auth.logout(request)
    return redirect("explore")

# Deleting user uploads


def delete_useruploads(request):
    if request.method == "POST":
        photo_id = request.POST.get('id')
        user_post = get_object_or_404(Photos, pk=photo_id, user=request.user)
        if user_post.file:
            user_post.file.delete(save=False)
        user_post.delete()
        messages.success(request, 'Photo deleted successfully.')
        return redirect('members')
    return redirect('explore')

