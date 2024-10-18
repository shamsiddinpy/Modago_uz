from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from shops.forms import SelectShopModelForm
from shops.models import ShopCategory, Country, Language, Currency, Shop
from users.models import Plan


class ShopCreationView(LoginRequiredMixin, CreateView):
    template_name = 'apps/shops/select-shop.html'
    form_class = SelectShopModelForm
    success_url = reverse_lazy('shop')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.plan = Plan.objects.get(name='Free Plan') 
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ShopCategory.objects.all()
        context['countrys'] = Country.objects.all()
        context['languages'] = Language.objects.all()
        context['currencys'] = Currency.objects.all()
        return context

    def form_invalid(self, form):
        return super().form_invalid(form)
