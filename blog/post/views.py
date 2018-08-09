from django.shortcuts import render, get_object_or_404, redirect
from post.forms import CommentForm, PostForm

from post.models import News, Com, NewP


def news_list(request):

    # BIBOD BSIX NOBIN
    news = News.objects.all()
                                                    #new = get_object_or_404(NewP,)
    posts = NewP.objects.filter()
    if request.method == "POST":
        form = PostForm(request.POST)
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect(news_list)
    else:
        form = PostForm()

    return render(request, "post/news_list.html", {"news": news, "posts": posts, "form": form})


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
