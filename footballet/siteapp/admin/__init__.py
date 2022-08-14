from django.contrib import admin
from siteapp.models import (
    EnglishSite as EnglishSiteModel,
    PersianSite as PersianSiteModel
)
from siteapp.admin.english import EnglishSiteAdmin
from siteapp.admin.persian import PersianSiteAdmin


admin.site.register(EnglishSiteModel,EnglishSiteAdmin)
admin.site.register(PersianSiteModel,PersianSiteAdmin)
