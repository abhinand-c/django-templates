from django.contrib import admin
from core import models

admin.site.site_header = "Admin Management System"
admin.site.index_title = "Welcome To Admin Management"
admin.site.site_title = "Primary Control Hub"


# Register your models here.
admin.site.register(models.User)
