from django.contrib import admin

# Register your models here.
from .models import *




class RickshawAdmin(admin.ModelAdmin):
    list_display = ('destination', 'fare',  'name', 'phone')


admin.site.register(Rickshaw,RickshawAdmin)


class VanAdmin(admin.ModelAdmin):
    list_display = ('destination', 'fare', 'time', 'name', 'phone')


admin.site.register(Van,VanAdmin)

class BusAdmin(admin.ModelAdmin):
    list_display = ('Route', 'fare', 'time', 'Book_Now' )


admin.site.register(Bus,BusAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject','message' )


admin.site.register(Contact,ContactAdmin)
