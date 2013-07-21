from django.db import models

from mongoengine import *
from datetime import *

class MOTD(Document):
    message = StringField()
    date = DateTimeField(default=datetime.now)

    def __unicode__(self):
        return self.date.strftime("%Y%m%d") + " - " + self.message

    def save(self, *args, **kwargs):
        self.date = datetime.now()
        super(MOTD, self).save(*args, **kwargs)

