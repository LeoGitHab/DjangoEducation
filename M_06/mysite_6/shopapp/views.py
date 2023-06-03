from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from shopapp.models import Product, Order
from .forms import ProductForm


def shop_index(request: HttpRequest):
    return HttpResponse('Hello World!')


def groups_list(request: HttpRequest):
    context = {
        'groups': Group.objects.prefetch_related('permissions').all(),
    }
    return render(request, 'shopapp/groups-list.html', context=context)


def products_list(request: HttpRequest):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'shopapp/products-list.html', context=context)


def create_product(request: HttpRequest) -> HttpResponse:
    form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'shopapp/create-product.html', context=context)


def orders_list(request: HttpRequest):
    context = {
        'orders': Order.objects.select_related('user').prefetch_related('products').all(),
    }
    return render(request, 'shopapp/orders-list.html', context=context)
