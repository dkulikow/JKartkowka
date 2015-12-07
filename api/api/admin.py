from django.contrib import admin

from api import *

admin.site.register(models.Lecturer)
admin.site.register(models.Group)
admin.site.register(models.Student)
admin.site.register(models.Test)
admin.site.register(models.Question)
admin.site.register(models.Answer)