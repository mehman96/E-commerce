from django.http import JsonResponse
from django.shortcuts import render,get_object_or_404
from .basket import Basket
from shop.models import *




def basket_summary(request):
    basket = Basket(request)
    return render(request, 'summary.html', {'basket': basket})



def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)

        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})
        return response


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': basketqty,'subtotal': baskettotal})
        return response


def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        basket.update(product=product_id, qty=product_qty)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': basketqty,'subtotal': baskettotal  })
        return response




def checkout(request):

    if request.method=="POST":       
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        town = request.POST['town']
        country = request.POST['country']
        phone = request.POST['phone']
        email = request.POST['email']
        company = request.POST['company']
        address = request.POST['address']
        user = Checkout(first_name=first_name, last_name=last_name, town=town,country=country,phone=phone,email=email,company=company,address=address)
        user.save()
        alert = True
        return render(request, 'checkout.html', {'alert':alert})
    return render(request, "checkout.html")

