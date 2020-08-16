from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)


"""
Webhooks are like the signals django sends each time a model is saved or deleted.
Except that they're sent securely from stripe to a URL we specify.
To handle these webhooks we're going to create our first custom class.
I'll create a new file here called webhook_handler.py
And start by importing HttpResponse from django.http
Now let's create a class called stripeWH_handler
And give it an init method.
The init method of the class is a setup method that's called every time an instance of the class is created.
For us we're going to use it to assign the request as an attribute of the class
just in case we need to access any attributes of the request coming from stripe.
Now I'll create a class method called handle event which will take the event stripe is sending us
and simply return an HTTP response indicating it was received.
"""
