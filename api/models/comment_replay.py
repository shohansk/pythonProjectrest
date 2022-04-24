from django.db import models
from api.models.comment import Comment
# Create your models here.
class CommentReplay(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    comment_re=models.ForeignKey(Comment,related_name='comment_replay',on_delete=models.CASCADE)
    comment_replay=models.CharField(max_length=4000)
    comment_replay_date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.comment_replay