from django.contrib import admin

# Register your models here.
from api.models.user_profile import UserProfile
from api.models.post import Post
from api.models.comment import Comment
from api.models.comment_replay import CommentReplay
admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(CommentReplay)