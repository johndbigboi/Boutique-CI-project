from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe

"""
    create a checkout view.
    For now it'll be pretty simple.
    First I'll get the bag from the session.
    And if there's nothing in the bag just add a simple error message.
    And redirect back to the products page.
    This will prevent people from manually accessing the URL by typing /checkout
    Next we just need to create an instance of our order form. Which will be empty for now.
    Then create the template.
    And the context containing the order form.
    And finally render it all out.
    We do need a couple imports at the top. We'll need to add redirect and reverse.
    Then messages from django.contrib
    And, of course, the order form.
    """


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
