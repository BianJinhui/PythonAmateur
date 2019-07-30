from django.db import models
from ckeditor.fields import RichTextField       #导入富文本
#1.数据库字段建模
#2.配置settings
#3.写视图页面
#4.改url

class Company(models.Model):
    name = models.CharField(max_length=32,verbose_name='公司名称')  #公司名称       或是改成varChar？
    address = models.TextField(verbose_name='公司地址')    #公司地址
    email = models.EmailField(verbose_name='公司邮箱')     #公司邮箱


#面试类型
class Type(models.Model):
    name = models.CharField(max_length=32,verbose_name='类型名称')  #类型名称
    description = models.TextField(verbose_name='类型描述')   #类型描述


#面试题
class interview(models.Model):
    title = models.CharField(max_length=32,verbose_name='标题') #标题
    content = RichTextField(verbose_name='内容')   #内容
    description = RichTextField(verbose_name='描述')   #描述
    Company_interview = models.ForeignKey(to=Company,on_delete = models.CASCADE,verbose_name='公司面试题')
    #一个公司多个面试题 一个面试题对应一个公司

# Create your models here.
