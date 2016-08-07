from django.contrib import admin
from members.models import Member
from members.models import Attend
from django.http import HttpResponse, HttpResponseForbidden
from members.actions import export_as_csv_action


class MemberAdmin(admin.ModelAdmin):
    fields = (
        'first_name',
        'middle_name',
        'last_name',
    )


class AttendAdmin(admin.ModelAdmin):
	list_display = ['attendee', 'date_attend']
	actions = [export_as_csv_action("CSV Export", fields=['attendee', 'date_attend'])]


admin.site.register(Attend, AttendAdmin)
admin.site.register(Member, MemberAdmin)
