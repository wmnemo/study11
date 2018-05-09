from django import forms
from .models import Post

# 유효성 검사
def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해주세요')

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'context']

class PostForm(forms.Form):
    title = forms.CharField(validators=[min_length_3_validator])
    context = forms.CharField(widget=forms.Textarea)