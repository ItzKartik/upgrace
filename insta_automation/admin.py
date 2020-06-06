from django.contrib import admin
from insta_automation import models

admin.site.register(models.insta_ids)


class Used_Inline(admin.TabularInline):
    model = models.left_ids


@admin.register(models.used_by)
class Main_Admin(admin.ModelAdmin):
    inlines = [
        Used_Inline
    ]
