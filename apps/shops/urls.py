from django.urls import path

from shops.views.base import BasedTemplateView
from shops.views.select_shop import SelectShopCreateView

urlpatterns = [
    path('dashboard/', BasedTemplateView.as_view(), name='shop'),
    path('select-shop', SelectShopCreateView.as_view(), name='select_shop'),
]
