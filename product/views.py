from .models import Products
from django.contrib.auth.models import User
from django.views.generic import (ListView, DetailView,
                                  UpdateView, DeleteView, CreateView, View)
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from mysite import settings
from django.db.models import Q


class Product_list(ListView):

    '''
    Display the product list
    '''
    template_name = "product/product_list.html"
    context_object_name = "product"

    def get_queryset(self):
        query = self.request.GET.get('search_product')
        if query:
            return Products.objects.filter(Q(user=self.request.user) & Q(name__icontains=query))
        else:
            return Products.objects.filter(user=self.request.user)


class Product_detail(DetailView):

    '''
    Display the product detail
    '''
    model = Products
    template_name = "product/product_detalis.html"
    context_object_name = "product"


class Product_edit(UpdateView):

    '''
    Display the product edit
    '''
    template_name = "product/product_edit.html"
    model = Products
    fields = ['name', 'photo', 'description']
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
    fields = ['name', 'photo', 'description']
    success_url = reverse_lazy("product:product_list")

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super(Product_save, self).form_valid(form)


class Logout(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)
