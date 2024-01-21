from django.views.generic import ListView

from main.models import Watch, Brand


class ShopView(ListView):
    template_name = 'pages/shop.html'
    model = Watch

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all()
        return context
