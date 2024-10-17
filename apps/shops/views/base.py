from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class BasedTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'apps/base.html'
