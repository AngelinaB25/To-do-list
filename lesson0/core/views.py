import random
from django.shortcuts import render
def index(request):
    return render(request,'main.html')
def sunday(request):
    todo_list = ['to do homework','to play with the cat','to go out with the dog']
    random.shuffle(todo_list)
    return render(request,'sunday.html',{'todo_list':todo_list})    
def monday(request):
    todo_1 = 'wash the dishes'
    return render(request,'monday.html',{'todo_1':todo_1})
def tuesday(request):
    return render(request,'tuesday.html')    



# Create your views here.
