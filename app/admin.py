from django.contrib import admin
from .models import Phones,Accounts,Address,Posts
#Register your models here.

# @admin.register(Accounts,Posts,Phones,Address)

# first way to customize the admin page
class addressAdmin(admin.ModelAdmin):
    # this customize the display of the model in admin page
    list_display=('street','city','state','zip')
    
    

# second way to customize the admin page with decorator
@admin.register(Address)
class addressAdmin(admin.ModelAdmin):
    # this customize the display of the model in admin page
    list_display=['street','city','state','zip']
    list_editable=['state']
    search_fields=['street']
    list_filter=['state']



# without customizing the admin page
# admin.site.register(Phones)
# admin.site.register(Accounts)
# admin.site.register(Address,addressAdmin)
# admin.site.register(Posts)



# to customize the admin page
# admin.site.register(Phones,adminCustomeClass)
# admin.site.register(Accounts,adminCustomeClass)
# admin.site.register(Address,adminCustomeClass)
# admin.site.register(Posts,adminCustomeClass)


