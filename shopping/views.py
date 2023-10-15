from django.shortcuts import render

# Create your views here.
def store(request):
    context = {}
    return render(request, 'shopping/store', context)

def cart(request):
    context = {}
    return render(request, 'shopping/cart', context)

def checkout(request):
    context = {}
    return render(request, 'shopping/checkout', context)