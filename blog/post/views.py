from django.shortcuts import render, get_object_or_404, redirect
from post.forms import CommentForm

from post.models import News, Com


def news_list(request):

    # BIBOD BSIX NOBIN
    news = News.objects.all()
    return render(request, "post/news_list.html", {"news": news})


def new_single(request, pk):
    #ВИВІД ВСІЄЇ СТАТІ
    new = get_object_or_404(News, id=pk)
    comment = Com.objects.filter(new=pk)#берем комент з бази + moderation=True якшо потрібно проходити провірку можератором

    if request.method == "POST":
        form = CommentForm(request.POST)
        #присвоюэм коменту користувача
        if form.is_valid():   #якшо пост то обробляэм і выдправляэм
            form = form.save(commit=False)
            form.user = request.user
            form.new = new
            form.save()
            return redirect(new_single, pk)
        #Якшо GET то відправляєм форму
    else:
        form = CommentForm()

    return render(request, 'post/new_single.html', {'new': new, "comments": comment, "form": form})
