from functools import reduce

from cart.apps import CartConfig
from main.models import Watch


def cart(request):
    cart = request.session.get(CartConfig.cart_session_key, [])
    cart_watches = Watch.objects.filter(id__in=cart)
    total_price = reduce(lambda x, y: x + y, [watch.price for watch in cart_watches], 0)
    return {
        'cart': {
            'total_price': total_price,
            'cart_watches': cart_watches
        }
    }
