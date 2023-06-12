from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html')

def password(request):
    the_password = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()-_=+/:;"<>?'))
    pass_length = int(request.GET.get('pass_len', 9))
    for char in range(pass_length):
        the_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': the_password})
