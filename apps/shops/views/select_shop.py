from django.views.generic import CreateView

from shops.forms import SelectShopModelForm


class SelectShopCreateView(CreateView):
    template_name = 'apps/shops/select-shop.html'
    form_class = SelectShopModelForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


