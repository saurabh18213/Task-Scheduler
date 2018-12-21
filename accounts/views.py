from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import Profile
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            profile = user.profile
            profile.image = form.cleaned_data["image"]
            profile.save()
            auth_login(request, user)
            return redirect('home')
    else:    
        form = SignUpForm()
    return render(request, 'signup.html', {'form' : form})

@login_required
def my_account(request):
    return render(request, 'my_account.html')