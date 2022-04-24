
from rest_framework import permissions
from api.permission.permission import IsOwnerOrReadOnly
from rest_framework import status, viewsets

from api.serializers.commentserializer import CommentSerializer
from api.models.comment import Comment


# Create your views here.
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)