from django.shortcuts import render
from django.views import View


class IndexView(View):
    context = {}
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.context)

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.context)
