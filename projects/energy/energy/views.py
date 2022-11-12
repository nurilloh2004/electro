
from django.shortcuts import render
from store.models import Product
from pages.models import Banner, Brand, Clients


def error_404(request, exception):
    return render(request, 'errors/404.html')

def error_500(request):
    return render(request, 'errors/404.html', status=500)


def home(request):
    
    top_products = Product.objects.filter(top=True)
    new_products = Product.objects.filter(new=True).order_by('-created_date')
    banner = Banner.objects.all()
    brand = Brand.objects.all()
    clients = Clients.objects.all()

    context = {
        'top':top_products,
        'new':new_products,
        'banner':banner,
        'brand':brand,
        'clients':clients,
    }
    return render(request, 'home.html', context)

def error_404(request, exception):
    return render(request, 'errors/404.html', status=404)

def error_500(request):
    return render(request, 'errors/404.html', status=500)
