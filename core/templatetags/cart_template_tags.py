from django import template
from core.models import Order

register = template.Library()

@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        order = Order.objects.filter(user=user, ordered=False)

        if order.exists():
            return order[0].items.count()
        else:
        	return 0

"""
In the python file, at first we have imported the tamplate from django and then imported the model we need 
for this functionality. Then we have created an instance of the template.Library() method. After all, to register 
the template we have used the decorators called "@register.filter" and then written a function which will return 
the total cart item count of the items we have in our order. That's it!
"""

"""
Development server won’t automatically restart

After adding the templatetags module, you will need to restart your server before you can use the tags 
or filters in templates.
"""