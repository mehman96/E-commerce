from .basket import Basket
from shop.models import *

def basket(request):
   return {'basket': Basket(request) }



def global_product_category(request):
    category = Category.objects.all()
    context={
        'category':category,
    }
    return context