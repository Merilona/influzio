from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def TestLogin(request):
    return render(request,'pages/login.html')
print('*************************************************************************************************')
print()
print('*************************************************************************************************')
def Testsignup(request):
    print('signup working')
    return render(request,'pages/sign-up.html')

import requests

print("Fetch api data from face book")



print("*********************Get User Data ***********************************************")




print("end  data")
import requests





import os
from django.conf import settings

# Use a raw string for the file path
csv_file = r"static/Inf.csv"
csv_file = os.path.join(settings.BASE_DIR, csv_file)

import csv
import json
new_data=[]
def csv_to_json(csv_file, json_file):
    # Open CSV file for reading
    with open(csv_file, 'r',encoding='utf-8') as csv_file:
        # Create a CSV reader
        csv_reader = csv.DictReader(csv_file)
        
        # Convert CSV data to a list of dictionaries
      
        global data
        data = list(csv_reader)
        for i in data:
            new_data.append(i)
    
        print(type(data))
        print(f"YYYYYYYYYYYYYYYYYYYYYYYYYY{len(data)}YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY")
        print(data[1])
        return data
      


        # Open JSON file for writi
print("****************************************************************************")
def Testexperimental(request):
        if request.user.is_authenticated:
            # print("user",request.user.username)
            
            # data=csv_to_json(csv_file,None)     
          
            # print("user",request.user.username)
        

            return render(request,'pages/exp2.html')
        else:
            print("currently user logout")
            return redirect('login')
from django.http import HttpResponse
          

def search_view(request,param):
    print(param)
    data=csv_to_json(csv_file,None)     
    print("my new data is awesome")
    print(type(data))
    print(data[:3:])
    print("Successssfully data")
    print("user",request.user.username)
    for user_data in data:
        if user_data.get('USERID') == param:
            return HttpResponse(f'The parameter passed is: {user_data}')
        
    

def index(request):
    return render(request,'Influzio Landing/index.html')


# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LoginForm

def signup_view(request):
    
    if request.user.is_authenticated:
        return redirect('exp')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print("i am here inside validation")
            return redirect('exp')
    else:
        form = SignUpForm()
        print("showing form")
    return render(request, 'pages/sign-up.html', {'form': form})
def login_view(request):
    print("user",request.user.username)

    if request.user.is_authenticated:
        return redirect('exp')

    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('exp')
    else:
        form = LoginForm()
    return render(request, 'pages/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')



def TermServices(request):
    return render(request,'pages/privacypolixy.html')



def TOS(request):
    return render(request,'pages/ToS.html')




