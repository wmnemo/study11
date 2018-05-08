from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    # name = 'Django'
    # return HttpResponse('''<h1>Hello {myname}</h1>
    # '''.format(myname=name))   정적인 내용
    # QuertSet 사용해서 글목록 가져오기
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #posts = Post.objects.filter(published_date__year='2018', published_date__month='05')
    return render(request, 'blog/post_list.html', {'posts':posts})