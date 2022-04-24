from rest_framework import serializers
from api.models.comment_replay import CommentReplay
class CommentReplaySerializer(serializers.ModelSerializer):
    replay_by = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = CommentReplay
       # fields = '__all__'
        fields = ['id', 'comment_re','comment_replay','comment_replay_date','replay_by']