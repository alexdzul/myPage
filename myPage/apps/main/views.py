from django.shortcuts import render, render_to_response, RequestContext


def index_view(request):
    return render_to_response('main/index.html', context_instance=RequestContext(request))
