from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Products
from django.shortcuts import redirect
from .forms import ProductForm
from django.contrib.auth.models import User
# Create your views here.

def product_list(request):
    product=Products.objects.all()
    return render(request,'product/product_list.html',{'product':product})


def product_save(request):
    if request.method == "POST":
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product/product_save.html', {'form': form})


def product_detail(request, pk):
    product=Products.objects.get(pk=pk)
    return render(request,'product/product_detalis.html',{'product':product})


def product_edit(request,pk):
    product=get_object_or_404(Products,pk=pk)
    if request.method=='POST':
        form=ProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            product=form.save(commit=False)
            product.save()
            return redirect('product_detail',pk=product.pk)
    else:
        form=ProductForm(instance=product)
    return render(request,'product/product_edit.html',{'form':form})
