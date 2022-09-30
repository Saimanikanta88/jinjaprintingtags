from django.shortcuts import render

# Create your views here.
def function1(request):
    return render(request,'one.html',context={'name':'saimanikanta','address':'bangalore','age':23})