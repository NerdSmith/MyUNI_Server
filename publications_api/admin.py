from django.contrib import admin

from publications_api.models import PubTag, PubGroup, Publication, PubPicture

admin.site.register(PubTag)
admin.site.register(PubGroup)
admin.site.register(Publication)
admin.site.register(PubPicture)
