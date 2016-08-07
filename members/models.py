from __future__ import unicode_literals
from django.db import models
from core.models import BaseModel


class Member(BaseModel):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return u'{0} {1} {2}'.format(self.first_name,  self.middle_name, self.last_name)

    def __str__(self):
        return self.__unicode__()


class Attend(models.Model):
    date_attend = models.DateTimeField(auto_now_add=True)
    attendee = models.ForeignKey(Member)

    def __unicode__(self):
        return u'{0} {1} {2} - {3}'.format(self.attendee.first_name, self.attendee.middle_name, self.attendee.last_name, self.date_attend.strftime('%d, %b %Y'))

    def __str__(self):
        return self.__unicode__()
