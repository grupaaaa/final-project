from django.views.generic import TemplateView

from shop.models import Category, OrderStatusChoice


class HomeView(TemplateView):
    template_name = "main/base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        if self.request.user.is_authenticated:
            context['order_id'] = self.request.user.order_set.filter(status=OrderStatusChoice.INITIAL).first().id
        return context