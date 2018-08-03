from django.contrib import admin
from post.models import News, Category, Tag, Com
from django_summernote.admin import SummernoteModelAdmin


class NewsAdmn(SummernoteModelAdmin):
    summernote_fields = ('text_min', 'text')


admin.site.register(News, NewsAdmn)
admin.site.register(Category)
admin.site.register(Tag)


class ComAdmn(admin.ModelAdmin):
    list_display = ("user", "new", "created", "moder")


admin.site.register(Com, ComAdmn)
