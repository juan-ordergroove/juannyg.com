import calendar
from django.db import models

from mongoengine import *
from datetime import *

YEARS = tuple((str(n), str(n)) for n in range(2013, datetime.now().year + 1))
MONTHS = tuple((i, calendar.month_abbr[i]) for i in xrange(1,13))

class Blog(Document):
    title = StringField(required=True, max_length=128)
    article = StringField(required=True)
    created = DateTimeField(default=datetime.now)
    month = IntField(default=datetime.now().month)
    year = IntField(default=datetime.now().year)
    meta = {
            'indexes': ['created', 'month', 'year']
        }

    def __unicode__(self):
        return self.created.strftime("%b %d, %Y") + " - " + self.title

