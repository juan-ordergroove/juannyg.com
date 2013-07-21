# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader

from main.models import MOTD

def index(request):
    motd = MOTD.objects.get()

    template = loader.get_template('main/index.html')
    context = Context({"motd": motd})
    return HttpResponse(template.render(context))
