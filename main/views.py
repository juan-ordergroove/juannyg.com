# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader

from main.models import MOTD

def index(request):
    try: motd = MOTD.objects.get()
    except: motd = ''

    template = loader.get_template('main/index.html')
    context = Context({"motd": motd})
    return HttpResponse(template.render(context))
