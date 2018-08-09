from django.forms import ModelForm
from django import forms
from.models import Com, News, NewP
#Форма коментів на сайті


class CommentForm(ModelForm):

    class Meta:
        model = Com
        fields = ("text",)


class PostForm(ModelForm):

    class Meta:
        model = NewP
        fields = ("text", "user", 'tags', "category","text_min")
