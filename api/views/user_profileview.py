
from api.models.user_profile import UserProfile
from rest_framework import viewsets
from rest_framework import permissions
from api.permission.permission import IsOwnerOrReadOnly
from api.serializers.userserializer import ProfileSerializer

# Create your views here.

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)