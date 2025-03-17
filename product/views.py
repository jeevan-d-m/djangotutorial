from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from employee.models import Employee
from django.template import loader
from .models import Category, Product
from django.core import paginator
from django.core.paginator import Paginator

from rest_framework import permissions, viewsets

from product.models import Brand, Category, Product
from product.serializers import BrandSerializer, CategorySerializer, ProductSerializer


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category.html', {'categories': categories})


def product_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)

    paginator = Paginator(products, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'product.html', {'page_obj': page_obj, 'category': category})


# try:
#         page_obj = paginator.page(page_number)
#     except (EmptyPage, PageNotAnInteger):
#         page_obj = None

class BrandViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Brand.objects.all().order_by('id')
    serializer_class = BrandSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Departments to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Departments to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
