from __future__ import unicode_literals
from django.db import models
from core.models import BaseModel


class Division(BaseModel):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return u'{0}'.format(self.name)

    def __str__(self):
        return self.__unicode__()

class Moi(BaseModel):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return u'{0}'.format(self.name)

    def __str__(self):
        return self.__unicode__()

class Zone(BaseModel):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return u'{0}'.format(self.name)

    def __str__(self):
        return self.__unicode__()

class Member(BaseModel):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    division = models.ForeignKey(Division, null=True)
    moi = models.ForeignKey(Moi, null=True)
    zone = models.ForeignKey(Zone, null=True)

    def __unicode__(self):
        return u'{0} {1} {2}'.format(self.first_name,  self.middle_name, self.last_name)

    def __str__(self):
        return self.__unicode__()


class Attend(models.Model):
    date_attend = models.DateTimeField(auto_now_add=True)
    attendee = models.ForeignKey(Member)

    def division(self):
        return self.attendee.division

    def moi(self):
        return self.attendee.moi

    def zone(self):
        return self.attendee.zone


    def __unicode__(self):
        return u'{0} {1} {2} - {3}'.format(self.attendee.first_name, self.attendee.middle_name, self.attendee.last_name, self.date_attend.strftime('%d, %b %Y'))

    def __str__(self):
        return self.__unicode__()
