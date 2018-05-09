from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from blog.modelforms import PostModelForm, PostForm
from .models import Post

# Create your views here.
# 글목록
def post_list(request):
    # name = 'Django'
    # return HttpResponse('''<h1>Hello {myname}</h1>
    # '''.format(myname=name))   정적인 내용
    # QuertSet 사용해서 글목록 가져오기
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #posts = Post.objects.filter(published_date__year='2018', published_date__month='05')
    return render(request, 'blog/post_list.html', {'posts': posts})

# 글 상세조회
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# 글 입력
def post_new(request):
    if request.method == "POST":
        form = PostModelForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostModelForm()
        print(form)  # 만들어주는 html 확인
    return render(request, 'blog/post_edit.html', {'form': form})

# 글등록 Form을 사용
def post_new_form(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        print(form)
        if form.is_valid():
            print(form.cleaned_data)
            post = Post(author=request.user, title=form.cleaned_data['title'], context=form.cleaned_data['context'], published_date=timezone.now())
            post.save()
            return redirect('post_detail', pk=post.pk)
        # 검증에 실패
        else:
            print(form.errors)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form':form})