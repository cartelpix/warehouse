from django import template

from orders.models import Order

register = template.Library()


@register.filter
def count_order_items(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, ordered=False)
        if qs.exists():
            return qs[0].items.count()
    return 0
