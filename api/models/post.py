from django.db import models
# Create your models here.
class Post(models.Model):
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    content=models.CharField(max_length=400)
    slug= models.CharField(max_length=50)
    post_image=models.ImageField(upload_to="post_image",null=True,blank=True)
    post_date=models.DateField(auto_now_add=True)
    category=models.CharField(max_length=100,default=None,blank=True,null=True)
    def __str__(self):
        return self.content