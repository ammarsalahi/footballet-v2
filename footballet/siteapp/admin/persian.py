from django.contrib import admin

class PersianSiteAdmin(admin.ModelAdmin):
    search_fields=['name']
    list_display=['name','url']
    list_filter=['name']