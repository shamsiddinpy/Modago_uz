from django.urls import path

from shops.views.base import BasedTemplateView
from shops.views.select_shop import WizardSelectShopTemplateView

urlpatterns = [
    path('', BasedTemplateView.as_view(), name='shop'),
    path('select-shop', WizardSelectShopTemplateView.as_view(), name='select_shop'),
]
