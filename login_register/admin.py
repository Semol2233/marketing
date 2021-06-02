from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.auth.models import  Group
admin.site.site_header = "Novus Marketing By HEY"

admin.site.unregister(Group)

admin.site.register(Loc)
admin.site.register(source)
admin.site.register(Marketing_update)
admin.site.register(status)









