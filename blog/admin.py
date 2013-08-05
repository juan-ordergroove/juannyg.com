from mongoadmin import site, DocumentAdmin

from blog.models import Blog

class BlogAdmin(DocumentAdmin):
    pass
site.register(Blog, BlogAdmin)
