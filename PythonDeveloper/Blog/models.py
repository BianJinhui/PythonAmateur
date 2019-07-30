from django.db import models
from ckeditor.fields import RichTextField

class Company(models.Model):
    name = models.CharField(max_length=32,verbose_name="公司名称")
    address = models.TextField(verbose_name='公司地址')
    email = models.EmailField(verbose_name="公司邮箱")

#面试类型
class type(models.Model):
    name = models.CharField(max_length=32,verbose_name="类行")
    description = models.TextField(verbose_name="类型描述")

#面试题类型
class interview(models.Model):
    title = models.CharField(max_length=32,verbose_name="标题")
    content = RichTextField(verbose_name="内容")
    description = RichTextField(verbose_name="描述")
    Company_interview = models.ForeignKey(to=Company, on_delete=models.CASCADE, verbose_name='公司面试题')

# Create your models here.
