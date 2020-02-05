from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Code
from .models import Page
from .models import Seo
from .models import Permit

admin.site.register(Code)
admin.site.register(Page)
admin.site.register(Seo)
admin.site.register(Permit)

admin.site.unregister(Group)
