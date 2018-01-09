from django.contrib import admin
from .models import Post,Category,Tag,About
# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ['title','author','created_time','id']


admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(About,PostAdmin)


