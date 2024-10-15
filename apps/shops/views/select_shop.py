from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView

from shops.forms import SelectShopModelForm
from shops.models import Shop, Category, ShopCategory, Country, Language, Currency


class ShopCreationView(CreateView):
    template_name = 'apps/shops/select-shop.html'
    form_class = SelectShopModelForm

    def get_queryset(self):
        return Shop.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ShopCategory.objects.all()
        context['countrys'] = Country.objects.all()
        context['languages'] = Language.objects.all()
        context['currencys'] = Currency.objects.all()
        return context
