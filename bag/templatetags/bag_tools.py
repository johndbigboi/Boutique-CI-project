from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    create a function called calc_subtotal
    Which takes in a price and a quantity as parameters and simply returns their irproduct.
    Now to register this filter we need to create a variable called register.
    Which is an instance of template.library
    And then use the register filter decorator to register our function as a template filter.
    All of this is straight from the django documentation by the way
    so if you'd like a deeper explanation of how it works
    just go there and look up creating custom template tags and filters.
    With the filter finished all we need to do to use it is load it in the bag template with load bag tools.
    Then we can pipe the price into it as the first argument.
    And send the item quantity as the second.
    """

    return price * quantity
