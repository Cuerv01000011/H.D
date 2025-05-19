from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('admin_dashboard' if user.is_staff else 'user_dashboard')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'accounts/login.html')


@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    return render(request, 'accounts/admin_dashboard.html')

@login_required
@user_passes_test(lambda u: not u.is_staff)
def user_dashboard(request):
    return render(request, 'accounts/user_dashboard.html')