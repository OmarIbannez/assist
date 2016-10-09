from django.contrib import admin
from members.models import (Member, Attend, Division, Moi, Zone, Group)
from django.http import HttpResponse, HttpResponseForbidden
from members.actions import export_as_csv_action


class MemberAdmin(admin.ModelAdmin):
    fields = (
        'first_name',
        'middle_name',
        'last_name',
        'division',
        'moi',
        'zone',
        'group',
    )

class DivisionAdmin(admin.ModelAdmin):
    fields = (
        'name',
    )

class MoiAdmin(admin.ModelAdmin):
    fields = (
        'name',
    )

class ZoneAdmin(admin.ModelAdmin):
    fields = (
        'name',
    )

class GroupAdmin(admin.ModelAdmin):
    fields = (
        'name',
    )

class AttendAdmin(admin.ModelAdmin):
    list_display = ('attendee', 'date_attend', 'division', 'moi', 'zone')
    list_filter = ('date_attend',)
    actions = [export_as_csv_action("CSV Export", fields=['attendee', 'date_attend', 'division', 'moi', 'zone'])]


admin.site.register(Attend, AttendAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Division, DivisionAdmin)
admin.site.register(Moi, MoiAdmin)
admin.site.register(Zone, ZoneAdmin)
admin.site.register(Group, GroupAdmin)
