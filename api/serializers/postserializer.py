
from rest_framework import serializers
from  api.serializers.commentserializer import CommentSerializer
from api.serializers.comment_replay import CommentReplaySerializer
from api.models.post import Post
class PostSerializer(serializers.ModelSerializer):
    posted_by = serializers.ReadOnlyField(source='owner.username')
    comments=CommentSerializer(many=True,read_only=True)
    comments_replay = CommentReplaySerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'posted_by','title','content','slug','post_image','category','post_date','comments','comments_replay']