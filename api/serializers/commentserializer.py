from rest_framework import serializers
from api.models.comment import Comment
class CommentSerializer(serializers.ModelSerializer):
    commented_by = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Comment
        fields = ['id', 'comment','comment_date','commented_by','post']