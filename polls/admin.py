from django.contrib import admin
from .models import Users,Album,Articles,Category,Leave

admin.site.register(Articles)
admin.site.register(Album)
admin.site.register(Users)
admin.site.register(Leave)
admin.site.register(Category)