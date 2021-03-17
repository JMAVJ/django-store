from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import View
from django.contrib import messages
from . import models


class Index(View):
    def get(self, request):
        context = {
            'products': models.Product.objects.all()
        }
        return render(request, 'index.html', context)


class Product(View):
    def get(self, request, id):
        context = {
            'product': models.Product.objects.get(id=id)
        }
        return render(request, 'product.html', context)


def add_product(request):
    if request.method != 'POST':
        return HttpResponse('Method not allowed')

    error = False

    if len(request.POST['name']) < 8:
        messages.error(request, 'The name must be at least 8 characters long')
        error = True
    elif float(request.POST['price']) <= 0:
        messages.error(request, 'The price must be greater than $0')
        error = True
    elif len(request.POST['description']) > 50:
        messages.error(request,
                       'The description can not be more than 50 characters long')
        error = True

    if error:
        return redirect('/')

    product = models.Product.objects.create(name=request.POST['name'], manufacturer=request.POST['manufacturer'],
                                            price=request.POST['price'], description=request.POST['description'])

    return redirect('/')


def delete_product(request, id):
    product = models.Product.objects.get(id=id)
    product.delete()
    return redirect('/')


def edit_product(request, id):
    if request.method != 'POST':
        return HttpResponse('Method not allowed')

    error = False

    if len(request.POST['name']) < 8:
        messages.error(request, 'The name must be at least 8 characters long')
        error = True
    elif float(request.POST['price']) <= 0:
        messages.error(request, 'The price must be greater than $0')
        error = True
    elif len(request.POST['description']) > 50:
        messages.error(request,
                       'The description can not be more than 50 characters long')
        error = True

    if error:
        return redirect('/')

    product = models.Product.objects.get(id=id)
    product.name = request.POST['name']
    product.manufacturer = request.POST['manufacturer']
    product.price = request.POST['price']
    product.description = request.POST['description']
    product.save()

    return redirect('/')
