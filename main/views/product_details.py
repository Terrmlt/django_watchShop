from django.views.generic import DetailView

from main.models import Watch


class ProductDetails(DetailView):
    template_name = 'pages/product-details.html'
    model = Watch
