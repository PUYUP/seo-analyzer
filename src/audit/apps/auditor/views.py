from django.shortcuts import render
from django.views import View
from django.http.response import JsonResponse

from apps.auditor.libs import analyzer


class AnalyzingAjaxView(View):
    context = {}

    def post(self, request, *agrs, **kwargs):
        self.context = {'daa': 'OK'}
        analyzer.run()
        return JsonResponse(self.context)
