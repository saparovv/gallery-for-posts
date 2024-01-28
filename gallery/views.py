from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.http import HttpResponse
from .forms import ProductForm



def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'index.html', context)


def details(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'details.html', context)


def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    context = {'form': form}
    return render(request, 'edit.html', context)


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product_list')



