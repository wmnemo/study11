from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    # 작성자
    author = models.ForeignKey('auth.user')
    # 제목
    title = models.CharField(max_length=200)
    # 내용
    context = models.TextField()
    # migrations test
    #test = models.TextField()
    # 작성일자
    create_date = models.DateTimeField(default=timezone.now)
    # 게시일
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()
