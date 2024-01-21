from django.views.generic import TemplateView

from cart.apps import CartConfig
from main.models import Watch


class CartView(TemplateView):
    template_name = 'pages/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        watch_ids = self.request.session.get(CartConfig.cart_session_key, [])
        context['watches'] = Watch.objects.filter(id__in=watch_ids)
        return context
