from django.urls import path

from shops.views.base import BasedTemplateView, DashboardView, CategoryTemplateView
from shops.views.select_shop import ShopCreationView

urlpatterns = [
    path('', BasedTemplateView.as_view(), name='shop'),
    path('dashboard/<str:pk>', DashboardView.as_view(), name='dashboard'),
    path('category', CategoryTemplateView.as_view(), name='category'),
    path('select-shop', ShopCreationView.as_view(), name='select_shop'),
]
