from mongoadmin import site, DocumentAdmin

from main.models import MOTD

class MOTDAdmin(DocumentAdmin):
    pass
site.register(MOTD, MOTDAdmin)
