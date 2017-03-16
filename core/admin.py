from django.contrib import admin

from core.models import DComment

class DCommentAdmin(admin.ModelAdmin):
    list_display = ['related', 'mail_reply']
    
admin.site.register(DComment,DCommentAdmin)
