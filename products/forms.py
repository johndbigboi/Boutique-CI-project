from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


"""
And have an inner metaclass that defines the model and the fields we want to include.
In this case I'm using a special dunder or double underscore string
called all which will include all the fields.
Then I'm going to override the init method to make a couple changes to the fields.
We'll want the categories to show up in the form using their friendly name.
So let's get all the categories.
And create a list of tuples of the friendly names associated with their category ids.
This special syntax is called the list comprehension.
And is just a shorthand way of creating a for loop that adds items to a list.
Now that we have the friendly names, let's update the category field on the form.
To use those for choices instead of using the id.
The effect of this will be seen in the select box that gets generated in the form.
Instead of seeing the category ID or the name field we'll see the friendly name.
Finally I'll just iterate through the rest of these fields
and set some classes on them to make them match the theme of the rest of our store.
"""
