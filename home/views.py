from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

# Create your views here.
def index(request):
    """A view that displays the index page"""
    return render(request, "index.html")