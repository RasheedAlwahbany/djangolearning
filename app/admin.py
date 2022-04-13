from django.contrib import admin
from .models import Phones,Accounts,Address,Posts
#Register your models here.
@admin.register(Accounts,Posts,Phones,Address)

class AuthorAdmin(admin.ModelAdmin):
    pass


# admin.site.register(Phones,AuthorAdmin)
# admin.site.register(Accounts,AuthorAdmin)
# admin.site.register(Address,AuthorAdmin)
# admin.site.register(Posts,AuthorAdmin)
