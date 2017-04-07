# coding:utf-8
from django import forms

from blog.models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost # 表单所基于的模型
        exclude = ('timestemp',) # 从生成的html中移除的表单项，注意保存方法
        widgets = {'body': forms.Textarea(attrs={'row':3,
                                                 'cols':50,
                                                 'style':'color:#f00'}),
                  } # 更改组件等操作
        labels = {
                  'body': u'内容',
        }
        
# class BlogPostForm(forms.Form):