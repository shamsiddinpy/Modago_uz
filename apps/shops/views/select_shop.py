from django.views.generic import TemplateView


class SelectShopTemplateView(TemplateView):
    template_name = 'apps/shops/select-shop.html'
