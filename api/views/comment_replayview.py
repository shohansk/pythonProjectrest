from rest_framework import permissions
from api.permission.permission import IsOwnerOrReadOnly
from rest_framework import status, viewsets

from api.serializers.comment_replay import CommentReplaySerializer
from api.models.comment_replay import CommentReplay


# Create your views here.
class CommentReplayViewSet(viewsets.ModelViewSet):
    queryset = CommentReplay.objects.all()
    serializer_class = CommentReplaySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)