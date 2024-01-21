from django.views.generic import TemplateView

from main.models import Watch


class HomeView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['watches'] = Watch.objects.all()[:9]
        return context
