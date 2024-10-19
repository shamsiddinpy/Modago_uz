from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class BasedTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'apps/base.html'


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'apps/dashboard/dashboard.html'


class CategoryTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'apps/shops/category.html'
