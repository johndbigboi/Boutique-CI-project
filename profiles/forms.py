from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False
    """
        Import forms from django
        And import our order model.
        Now I'll create a new order form class.
        And give it a couple meta options telling django which model it'll be associated with.
        and which fields we want to render.
        Notice here that we're not rendering any fields in the form which will be automatically calculated.
        And that's because no one will ever be filling that information out.
        It'll all be done via the model methods we've created.
        We're also going to override the init method of the form which will allow us to customize it quite a bit.
        I'll paste this method in and go through it.
        First we call the default init method to set the form up as it would be by default.
        After that, I've created a dictionary of placeholders which will show up
        in the form fields rather than having clunky looking labels and empty text boxes in the template.
        Next we're setting the autofocus attribute on the full name field to true
        so the cursor will start in the full name field when the user loads the page.
        And finally we iterate through the forms fields adding a star to the placeholder
        if it's a required field on the model.
        Setting all the placeholder attributes to their values in the dictionary above.
        Adding a CSS class we'll use later.
        And then removing the form fields labels.
        Since we won't need them given the placeholders are now set.
        If this doesn't make complete sense take some time to experiment and tear this code apart.
        This is fairly advanced form customization,
        and it should give you a good idea of just how powerful Django can be if you know it well.
        With that done we've got an order form ready to go.
        Our models and signals connected.
        And the admin customized.
        So I'm going to commit my changes
        And in the next video, we'll create the first view for the checkout system
        and begin designing the check out template.
    """
