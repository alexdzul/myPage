from django.shortcuts import render, render_to_response, RequestContext
from myPage.apps.social.models import SocialNetwork
from myPage.apps.main.models import Setting

def index_view(request):
    redes = SocialNetwork.objects.filter(status=True)
    sett = Setting.objects.filter(status=True)[0]
    ctx = {'networks':redes, 'settings':sett}
    return render_to_response('main/index.html', ctx, context_instance=RequestContext(request))
