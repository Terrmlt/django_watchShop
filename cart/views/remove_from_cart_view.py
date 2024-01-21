from django.http import HttpResponseRedirect
from django.views import View

from cart.apps import CartConfig


class RemoveFromCartView(View):
    def post(self, request, *args, **kwargs):
        pk = kwargs['pk']
        cart = request.session.get(CartConfig.cart_session_key, [])
        cart.remove(int(pk))
        request.session[CartConfig.cart_session_key] = cart
        return HttpResponseRedirect(redirect_to=request.META['HTTP_REFERER'])
