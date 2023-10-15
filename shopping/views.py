from django.shortcuts import render

# Create your views here.
def store(request):
    context = {}
    return render(request, 'shopping/store.html', context)

def cart(request):
    context = {}
    return render(request, 'shopping/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'shopping/checkout.html', context)