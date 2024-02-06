# myapp/views.py
from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.hashers import make_password, check_password
import jsonify
from django.http import JsonResponse

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        hashed_password = make_password(password)

        print(username)
        print(password)
        User.objects.create(username=username, password=hashed_password, email=email)


        return redirect('login')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.get(username=username)

        if check_password(password, user.password):
            print("seccess")
            # Successful login
            # You can add session handling or any other logic here
            return redirect('home')
            # return JsonResponse({"data": "Logged is success"})
        else:
            # Failed login
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')
    # return "Logged in suceesss"
