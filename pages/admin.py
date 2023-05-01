from django.contrib import admin
from . import models
# Register your models here.
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered

from django.contrib.auth.models import Group,User

# admin.site.unregister(Group)
# admin.site.unregister(User)




app_models = apps.get_app_config('pages').get_models()
for model in app_models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
    

class SystemAdmin(admin.ModelAdmin):
    filter_horizontal = ('words',) 

# admin.site.unregister(models.groups)
# admin.site.register(models.groups,SystemAdmin)







# admin.site.unregister(models.words)
# @admin.register(models.words)
# class PersonAdmin(admin.ModelAdmin):
#     list_display = ("en_word", "ar_word")
#     filter_horizontal = ('sentences',) 
#     search_fields = ("en_word", )