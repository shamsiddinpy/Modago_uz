from django.urls import path

from shops.views.base import BasedTemplateView, DashboardView
from shops.views.category import CategoryCreateViewListView
from shops.views.select_shop import ShopCreationView

app_name = 'shops'
urlpatterns = [
    path('', BasedTemplateView.as_view(), name='shop'),
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('category', CategoryCreateViewListView.as_view(), name='category'),
    path('select-shop', ShopCreationView.as_view(), name='select_shop'),
]
