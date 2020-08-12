from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal')
)


"""
required is often used to make the field optional that is the user would no longer be required to enter the data 
into that field and it will still be accepted. By default, each Field class assumes the value is required. 
So, to make it 'not required' you need to set 'required=False'

"It's a form validator"

""" 
class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(required=False)
    shipping_address2 = forms.CharField(required=False)
    shipping_country = CountryField(blank_label='(select country)').formfield(required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        })) #See the comment at the very bottom
    shipping_zip = forms.CharField(required=False)
    

    billing_address = forms.CharField(required=False)
    billing_address2 = forms.CharField(required=False)
    billing_country = CountryField(blank_label='(select country)').formfield(required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    billing_zip = forms.CharField(required=False)


    same_billing_address = forms.BooleanField(required=False)
    set_default_shipping = forms.BooleanField(required=False)
    use_default_shipping = forms.BooleanField(required=False)
    set_default_billing = forms.BooleanField(required=False)
    use_default_billing = forms.BooleanField(required=False)

    payment_option = forms.ChoiceField(widget=forms.RadioSelect, choices=PAYMENT_CHOICES)

"""
Use "blank_label" to set the label for the initial blank choice shown in forms:

country = CountryField(blank_label='(select country)')

This field can also allow multiple selections of countries. The field will always output a list of countries in 
this mode.



CountrySelectWidget:-

A widget is included that can show the flag image after the select box 
(updated with JavaScript when the selection changes).
"""

class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Promo code',
        'aria-label': 'Recipient\'s username',
        'aria-describedby': 'basic-addon2'
    }))



class RefundForm(forms.Form):
    ref_code = forms.CharField()
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4
    }))
    email = forms.EmailField()



class PaymentForm(forms.Form):
    stripeToken = forms.CharField(required=False)
    save = forms.BooleanField(required=False)
    use_default = forms.BooleanField(required=False)


"""
'attrs' = attributes.
ek kothay bolte gele ukto input field ti ke bivinno styling dewa. ekhane bootstrap class attribute er vetor 
duto attribute value dewa hoyese. attribute joto ichcha dewa jay ebong onnovabew dewa jay. jemon: CouponForm
"""


"""
Whenever you specify a field on a form, Django will use a default widget that is appropriate to the type of data 
that is to be displayed. However, if you want to use a different widget for a field, you can use the widget 
argument on the field definition. For example:

from django import forms

class CommentForm(forms.Form):
    name = forms.CharField()
    url = forms.URLField()
    comment = forms.CharField(widget=forms.Textarea)

This would specify a form with a comment that uses a larger Textarea widget, rather than the default 
TextInput widget.

"""