from django.contrib import admin
from .models import Posts
from .models import Actor,Table,RegUser

admin.site.register(Posts)
admin.site.register(Actor)
admin.site.register(Table)
admin.site.register(RegUser)
# Register your models here.
