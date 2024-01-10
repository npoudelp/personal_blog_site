from django.contrib import admin
from .models import post


# Register your models here.

class TinyMCEAdmin(admin.ModelAdmin):
    class Media:
        js = ('/static/tinymce_6.8.2/tinymce/js/tinymce/tinymce.min.js', )


admin.site.register(post, TinyMCEAdmin)