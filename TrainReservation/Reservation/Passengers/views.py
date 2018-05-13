from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from . import forms
from django.contrib.auth.decorators import login_required
from .models import PassengerReview

def signup_view(request):
    if request.method == 'POST':
        signupForm = UserCreationForm(request.POST)
        if signupForm.is_valid():
            user = signupForm.save()
            login(request, user)
            return redirect('Passengers:intermediate_view')
    else:
        signupForm = UserCreationForm()
    return render(request, 'Passengers/signup.html', {'form':signupForm})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('Passengers:intermediate_view')
    else:
        form = AuthenticationForm()

    return render(request, 'Passengers/login.html', {'loginForm': form})

@login_required(login_url="../../Passengers/PassengerLogin/")
def intermediate_view(request):
    return render(request, 'Passengers/intermediate.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return render(request, 'index.html')

@login_required(login_url="../../Passengers/PassengerLogin/")
def review_view(request):
    if request.method == 'POST':
        form = forms.PassengerReview(request.POST, request.FILES)
        if form.is_valid():
            reviewInstance = form.save(commit=False)
            reviewInstance.author = request.user
            reviewInstance.save()
            return redirect('Passengers:review_created')
    else:
        form = forms.PassengerReview()

    return render(request, 'Passengers/review.html', {'PassengerReviewForm':form})

def review_created(request):
    return render(request, 'Passengers/reviewCreated.html')

@login_required(login_url="../../Passengers/PassengerLogin/")
def profile(request):
    instanceReview = PassengerReview.objects.all().order_by('title')
    return render(request, 'Passengers/profile.html', {'review': instanceReview})