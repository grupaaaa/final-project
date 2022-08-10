from django.views.generic import TemplateView

from shop.models import Category


class HomeView(TemplateView):
    template_name = "main/base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context