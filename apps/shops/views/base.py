from django.views.generic import TemplateView


class BasedTemplateView(TemplateView):
    template_name = 'apps/base.html'
