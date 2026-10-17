from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm, StudentProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):

    if request.method == 'POST':
        user_form = StudentRegistrationForm(request.POST)
        profile_form = StudentProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)

            return redirect('dashboard')

    else:
        user_form = StudentRegistrationForm()
        profile_form = StudentProfileForm()

    return render(
        request,
        'accounts/register.html',
        {
            'user_form': user_form,
            'profile_form': profile_form
        }
    )


def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        return render(
            request,
            'accounts/login.html',
            {'error': 'Invalid username or password'}
        )

    return render(request, 'accounts/login.html')

@login_required
def dashboard(request):

    return render(
        request,
        'accounts/dashboard.html'
    )

def user_logout(request):

    logout(request)

    return redirect('login')
