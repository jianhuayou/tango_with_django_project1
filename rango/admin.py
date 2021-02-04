from django.contrib import admin
from rango.models import Category, Page
# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','url')

class CategoryAdmin(admin.ModelAdmin):
    lisst_display = ('views','likes')

admin.site.register(Category,CategoryAdmin)
admin.site.register(Page,PageAdmin)