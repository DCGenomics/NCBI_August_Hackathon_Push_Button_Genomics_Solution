from django.views import generic
from django.shortcuts import render

from .models import Gene


class IndexView(generic.TemplateView):
    template_name = 'browser/index.html'


class UploadView(generic.TemplateView):
    template_name = "browser/upload.html"

    def get(self, request):
        return render(request, self.template_name, {"foo": "asdfasdf"})


class ResultsView(generic.TemplateView):
    template_name = "browser/results.html"

    def get_context_data(self, **kwargs):
        context = super(ResultsView, self).get_context_data()

        context['genes_all'] = Gene.objects.all()[:5]

        context["filters"] = [
            ["Clinical significance", "Pathogenic"],
            ["Molecular consequence", "Missense"]
        ]

        context["genes"] = [
            {
                "symbol": "BRCA",
                "id": "672",
                "length": "81,189",
                "pathogenic_variants": "4",
                "benign_variants": "50",
                "missense_variants": "3",
                "synonymous_variants": "130"
            },
            {
                "symbol": "APOE",
                "id": "348",
                "length": "3,647",
                "pathogenic_variants": "0",
                "benign_variants": "2",
                "missense_variants": "0",
                "synonymous_variants": "11"
            },
            {
                "symbol": "MLH1",
                "id": "4292",
                "length": "2,662",
                "pathogenic_variants": "13",
                "benign_variants": "2",
                "missense_variants": "10",
                "synonymous_variants": "0"
            }
        ]

        return context
