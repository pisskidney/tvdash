from tvdash.models import SourceWebsite
from django.shortcuts import render_to_response
from tvdash.forms import SearchForm


def index(request):
    search_form = SearchForm({13: "Cast Away", 1443: "Gone baby gone"})
    return render_to_response('tvdash/index.html', {
        'search_form': search_form,
    })


def search(request):
    sources = list()
    for source in SourceWebsite.objects.all():
        source.url_search = source.url_search.replace(
            "(*)", request.GET['query']
        )
        sources.append(source)

    return render_to_response('tvdash/search.html', {
        'sources': sources,
    })
