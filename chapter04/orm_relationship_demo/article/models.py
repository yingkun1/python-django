from django.db import models

def default_category():
    return Category.objects.get(pk=4)

class Category(models.Model):
    name = models.CharField(max_length=100)

class Tag(models.Model):
    name = models.CharField(max_length=100)
    article = models.ManyToManyField("Article",related_name="tags")

class Article(models.Model):
    title = models.CharField(max_length=100)
    context = models.TextField()
    category = models.ForeignKey("Category",on_delete=models.DO_NOTHING,null=True,related_name='articles')
    author = models.ForeignKey("frontuser.FrontUser",on_delete=models.CASCADE,null=True)

    def __str__(self):
        return ("(<Article> id:%s,title:%s,context:%s,category_id:%s,author_id:%s)"%(self.id,self.title,self.context,self.category_id,self.author_id))

class Comment(models.Model):
    content = models.TextField()
    origin_comment = models.ForeignKey("article.Comment",on_delete=models.CASCADE)

#category:
#id,name
#1,最新

#article:
#id,title,category
#1,xxx,1