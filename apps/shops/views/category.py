from django.views.generic import CreateView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType

from shops.forms import CategoryModelForm
from shops.models import Category, Attachment


class CategoryCreateViewListView(LoginRequiredMixin, CreateView):
    template_name = 'apps/shops/category.html'
    form_class = CategoryModelForm
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def form_invalid(self, form):
        return super().form_invalid(form)
