from django.contrib import admin

from lblog.models import Blog, Theme, Category, Tag, Topic

class BlogAdmin(admin.ModelAdmin):
	list_display = ('title', 'theme', 'category', 'author', 'publish_time', 'update_time')
	list_filter = ('publish_time',)
	date_hierarchy = 'publish_time'
	ordering = ('-publish_time',)
	filter_horizontal = ('tags',)

class CAdmin(admin.ModelAdmin):
	fields = ['name']
	list_display = ['name', 'count', 'created']

admin.site.register(Blog, BlogAdmin)
admin.site.register([Theme, Category, Tag, Topic], CAdmin)
