from webbrowser import Grail
from django.contrib import admin
from .models import *
# Register your models here.
class MyAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount')

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Book)
admin.site.register(Store)
admin.site.register(TransactionAtomicityModel,MyAdmin)
admin.site.register(Group)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Post2)
admin.site.register(product)