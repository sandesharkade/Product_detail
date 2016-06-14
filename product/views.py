from .models import Products
from django.contrib.auth.models import User
from django.views.generic import (ListView, DetailView,
                                  UpdateView, DeleteView, CreateView, View)
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from mysite import settings
from django.shortcuts import render


class Product_list(ListView):

    '''
    Display the product list
    '''
    template_name = "product/product_list.html"
    context_object_name = "product"

    def get_queryset(self):
        return Products.objects.filter(user=self.request.user)


class Product_detail(DetailView):

    '''
    Display the product detail
    '''

    model = Products

    template_name = "product/product_detalis.html"
    context_object_name = "product"

    # def get(self, request, pk):
        # return Products.objects.filter(user=self.request.user, id=pk)
        # return render(request, 'product/product_detalis.html', {'product':
        # product})


class Product_edit(UpdateView):

    '''
    Display the product edit
    '''

    template_name = "product/product_edit.html"
    model = Products
    fields = ['pname', 'photo', 'description']
    success_url = reverse_lazy("product:product_list")


class Product_delete(DeleteView):

    '''
     product delete
    '''

    model = Products
    success_url = reverse_lazy("product:product_list")


class Product_save(CreateView):

    '''
     product save
    '''
    model = Products
    template_name = "product/product_save.html"
    fields = ['pname', 'photo', 'description']
    success_url = reverse_lazy("product:product_list")

    def form_valid(self, form):
        print(self.request.user)

        user = self.request.user
        form.instance.user = user

        return super(Product_save, self).form_valid(form)


class Logout(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)
