from django.shortcuts import render
from products.models import Product
from django.core.urlresolvers import reverse_lazy

# Create your views here.
def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})