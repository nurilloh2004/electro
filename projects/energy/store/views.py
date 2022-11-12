from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order, OrderItem
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.core.paginator import Paginator

from category import models
from category.models import Category, MetaDetail
from carts.models import Cart, CartItem
from .forms import OrderForm



def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        met = MetaDetail.objects.filter(category__slug=category_slug)
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category_id__in=[item.id for item in category.get_descendants(include_self=True)], is_available=True).order_by('-created_date')
        paginator = Paginator(Product.objects.filter(category_id__in=[item.id for item in category.get_descendants(include_self=True)], is_available=True).order_by('-created_date'), 15)
        page_num = request.GET.get('page')
        page = paginator.get_page(page_num)
    else:
        products = Product.objects.all()

        paginator = Paginator(products, 15)
        page_num = request.GET.get('page')
        page = paginator.get_page(page_num)

    context = {
        'products': products,
        'page': page,
        'met': met,
    }
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    new_products = Product.objects.filter().order_by('-created_date')[:10]
    context = {
        'single_product': single_product,
        'new': new_products,
    }
    return render(request, 'store/product_detail.html', context)


def store_category(request):

    category = Category.objects.all()

    paginator = Paginator(category, 15)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    context = {
        'category':category,
        'page': page,
    }
    return render(request, 'store/category.html', context)


def checkout(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Order(**form.cleaned_data)
            order.save()
            try:
                cart = Cart.objects.filter(cart_id=_cart_id(request)).first()
                cart_items = CartItem.objects.filter(cart=cart, is_active=True)
                for cart_item in cart_items:
                    order_item = OrderItem(
                        order=order,
                        product=cart_item.product,
                        quantity=cart_item.quantity
                    )
                    order_item.save()
                cart_items.update(is_active=False)
                cart.is_active = False
                cart.save()
                return redirect('complete')
            except ObjectDoesNotExist:
                pass
    return render(request,  'store/checkout.html')


def complete(request):
    return render(request, 'store/thanks.html')


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            product_search = Product.objects.order_by('-created_date').filter(Q(translations__description__icontains=keyword) | Q(translations__product_name__icontains=keyword))
            product_count = product_search.count()
    context = {
        'product_search': product_search,
        'product_count': product_count,
    }
    return render(request, 'store/search.html', context)