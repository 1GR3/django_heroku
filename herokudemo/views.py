from django.views.generic import TemplateView


class MyView(TemplateView):
    template_name = 'sample.html'

