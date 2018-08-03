from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    title = models.CharField("Name", max_length=50)

    verbose_name = "Kategoria"
    verbose_name_plural = "Kategorii"

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField("TAG", max_length=50)

    verbose_name = "TEG"
    verbose_name_plural = "TEGI"

    def __str__(self):
        return self.title


class News(models.Model):
    user = models.ForeignKey(User,
                             verbose_name="АВТОР",
                             on_delete=models.CASCADE)

    category = models.ForeignKey(Category,
                                 verbose_name="KATEGORIA",
                                 on_delete=models.SET_NULL,
                                 null=True)
    title = models.CharField("Zagolobok",
                             max_length=150)
    text_min = models.TextField("malenkii_text",
                                max_length=400)
    text = models.TextField("TUT_POLNII_text_STATI")
    tags = models.ManyToManyField(Tag,
                                  verbose_name="TEGI")
    created = models.DateTimeField("KOGDA_sozd",
                                   auto_now_add=True)
    description = models.CharField("opisanie",
                                   max_length=100)
    keywords = models.CharField("KLU4eBIE_SLOBA",
                                max_length=50)

    verbose_name = "Stat'a"
    verbose_name_plural = "Stat'ii"

    def __str__(self):
        return self.title


class Com(models.Model):

    #Клас коментів до новин

    user = models.ForeignKey(User, verbose_name="PolsoBatel'",
                             on_delete=models.CASCADE)

    new = models.ForeignKey(News,
                            verbose_name="Koment",
                            on_delete=models.CASCADE)

    text = models.TextField("KOMENT")

    created = models.DateTimeField("Data",
                                   auto_now_add=True,
                                   null=True)
    moder = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Koment"
        verbose_name_plural = "Komenti"

        def __str__(self):
            return self.title