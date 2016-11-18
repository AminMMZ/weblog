from django.shortcuts import render
from django.http.response import HttpResponse

from blog.forms import CommentForm
from blog.models import Post, Comment


# Create your views here.
def show_all_posts(request):
    pg = 1;
    if request.method=='GET' and 'pg' in request.GET:
        pg = int(request.GET.get('pg'))
        print pg
    posts = Post.objects.filter(id__gt=(pg-1)*10,id__lte=pg*10).order_by('-date')
    if (len(posts)==0):
        return HttpResponse('Not Found 404')
    else:
        template = 'index.html'
        return render(request, template, {'prv':pg-1,'nxt':pg+1,'posts': posts})


def show_post(request):
    pid = request.GET.get('pid')
    pst = Post.objects.get(id=pid)
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            cm = Comment(post=pst,name=form.cleaned_data['name'],text=form.cleaned_data['text'])
            cm.save()
            comments = pst.comment_set.all()
    comment_form = CommentForm()
    count = len(comments)
    template = 'post.html'
    return render(request, template, {'post': pst, 'count': count, 'comment_form':comment_form,'comments': comments})
