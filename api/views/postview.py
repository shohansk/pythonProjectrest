

from  api.serializers.postserializer import PostSerializer
from api.models.post  import Post
from rest_framework import permissions
from api.permission.permission import IsOwnerOrReadOnly

from rest_framework import status, viewsets

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]



    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)