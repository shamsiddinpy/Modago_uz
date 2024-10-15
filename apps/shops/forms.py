from django.forms import ModelForm

from shops.models import Shop


class SelectShopModelForm(ModelForm):
    class Meta:
        model = Shop
        fields = 'name', 'shop_category', 'phone', 'country', 'languages', 'currency'

