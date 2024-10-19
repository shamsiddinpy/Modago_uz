from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from shops.models import Shop


class BasedTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'apps/base.html'


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'apps/dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        shop = Shop.objects.get(pk=kwargs['pk'])
        context['shop'] = shop
        return context


class CategoryTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'apps/shops/category.html'
