from django.shortcuts import render, get_object_or_404

from cart.forms import CartAddProductForm
from .models import Category, Product


def product_list(request, category_slug=None):
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        products = Product.objects.filter(category=category)
    else:
        category = None
        products = Product.objects.filter(available=True)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


