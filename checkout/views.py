from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import Settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe
# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51S1P9CDNb7zK3OXzVk64NLDZKB1UTxL08GXm1nprD0E94av1UXURTBDdYI2FZI74FJHoHCFp0WO1qSm1Pu6nL4Dr00QEllNA1t',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)