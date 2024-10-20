from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView

from shops.models import Shop


class BasedTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'apps/base.html'


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'apps/dashboard/dashboard.html'

    def get(self, request, *args, **kwargs):
        shop_id = request.session.get('shop_id', None)
        if not shop_id:
            return redirect('shops:select_shop')

        shop = Shop.objects.get(pk=shop_id)
        context = self.get_context_data(shop=shop)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shop'] = kwargs.get('shop')
        return context
