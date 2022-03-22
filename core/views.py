from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, num1, num2):
    #return HttpResponse('<h1>Hello {} de {} anos</h1>' .format(nome, idade))
    total = num1 + num2
    return HttpResponse('<h1>Soma de {} e {} é igual a {}</h1>'.format(num1, num2, total))