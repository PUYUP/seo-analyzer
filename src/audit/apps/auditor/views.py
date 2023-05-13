from django.shortcuts import render
from django.views import View
from django.http.response import JsonResponse

from apps.auditor.libs import analyzer


class AnalyzingAjaxView(View):
    context = {
        'output': None,
        'word_count': 0,
        'internal_link_count': 0,
        'keywords': [],
        'title': None,
        'description': None,
        'warnings': [],

    }

    def post(self, request, *agrs, **kwargs):
        url = request.POST.get('url')

        output = analyzer.run(url)
        self.context.update({'output': output})

        if 'pages' in output:
            page = output['pages'][0]
            word_count = page.get('word_count', 0)
            keywords = page.get('keywords', [])
            title = page.get('title', None)
            description = page.get('description', None)
            warnings = page.get('warnings', [])

            self.context.update({
                'word_count': word_count,
                'internal_link_count': len(output['pages']),
                'keywords': keywords,
                'title': title,
                'description': description,
                'warnings': warnings,
            })

        return JsonResponse(self.context)
