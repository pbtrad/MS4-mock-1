from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe


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
        'stripe_public_key': 'pk_test_51IMnacJM4wvtkePbYBUsu09c7T8jZwAJPSjpnPJbM2x2JavW0VxJs2OHo4szK6CVjzATDLucIxwPiwf8JPzskpOy00LEw5XZum',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)