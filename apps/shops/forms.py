from django import forms
from django.forms import ModelForm, ClearableFileInput, FileInput

from shops.models import Shop, Category, Attachment


class SelectShopModelForm(ModelForm):
    class Meta:
        model = Shop
        fields = 'name', 'shop_category', 'phone', 'country', 'languages', 'currency'


class CategoryModelForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'emoji', 'parent', 'description', 'position']
