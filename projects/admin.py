from django.contrib import admin
from .models import Project, Review, Tag 


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title','created_at','owner']


class ReviewAdmin(admin.ModelAdmin):
        list_display = ['project','value','owner']

admin.site.register(Project, ProjectAdmin)
admin.site.register(Review, ReviewAdmin )
admin.site.register(Tag  )