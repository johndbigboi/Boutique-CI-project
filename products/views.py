from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
"""
Jango.db.models called Q to generate a search query.
This deserves a bit of an explanation.
In Jango if you use something like product.objects.filter
In order to filter a list of products. Everything will be ended together.
In the case of our queries that would mean that when a user submits a query.
In order for it to match the term would have to appear in both the product name and the product description.
Instead, we want to return results where the query was matched in either
the product name or the description.
In order to accomplish this or logic, we need to use Q
"""

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    """
    we'll start with it as none at the top of this view to ensure we don't get an error
    when loading the products page without a search term.
    """
    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            """
            double underscore syntax is common when making queries in django.
Using it here means we're looking for the name field of the category model.
And we're able to do this because category and product are related with a foreign key.

            This might seem redundant but remember that by doing this
we're converting the list of strings of category names passed through the URL
into a list of actual category objects, so that we can access all their fields in the template.
Let's call that list of category objects, current_categories.

            """

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            """
            the code using Q is actually quite simple.
            I'll set a variable equal to a Q object. Where the name contains the query.
            Or the description contains the query.
            The pipe here is what generates the or statement.
            And the i in front of contains makes the queries case insensitive.
            """
            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
