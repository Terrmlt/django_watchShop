from django.http import HttpResponseRedirect
from django.views import View

from cart.apps import CartConfig
from main.models import Watch


class AddInCartView(View):
    def post(self, request, *args, **kwargs):
        pk = kwargs['pk']
        book = Watch.objects.get(id=pk)

        cart = request.session.get(CartConfig.cart_session_key, [])

        if book.id not in cart:
            cart.append(book.id)

        request.session[CartConfig.cart_session_key] = cart

        return HttpResponseRedirect(redirect_to=request.META['HTTP_REFERER'])
