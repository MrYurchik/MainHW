from django.forms import ModelForm

from.models import Com
#Форма коментів на сайті


class CommentForm(ModelForm):

    class Meta:
        model = Com
        fields = ("text",)
