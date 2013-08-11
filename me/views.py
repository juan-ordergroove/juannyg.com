from django.http import HttpResponse
from django.template import Context, loader

def index(request):
    template = loader.get_template('me/index.html')
    return HttpResponse(template.render(Context()))
