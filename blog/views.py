# Create your views here.
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.template import Context, loader

from blog.models import Blog

def _page_blogs(page):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 5)
    try: blogs = paginator.page(page)
    except: blogs = paginator.page(1)
    return blogs

def blog_page(request, page):
    template = loader.get_template('blog/left.html')
    context = Context({"blogs": _page_blogs(page)})
    return HttpResponse(template.render(context))

def index(request):
    blogs = _page_blogs(1)
    template = loader.get_template('blog/index.html')
    context = Context({"blogs": blogs})
    return HttpResponse(template.render(context))
