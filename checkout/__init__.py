default_app_config = 'checkout.apps.CheckoutConfig'
"""
First in checkouts __innit__.py we need to tell django the name of the default config class for the app
which is checkout.apps.CheckoutConfig.
You may remember this class from apps.py where we imported our signals module.
Without this line in the innit file, django wouldn't know about our
custom ready method so our signals wouldn't work.
If your server is running right now you'll need to restart it for this to take effect.
"""
