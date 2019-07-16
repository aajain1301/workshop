from rest_framework import viewsets, permissions,generics

from registration.models import User
from .serializers import UserSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     permission_classes = [permissions.AllowAny, ]
#     serializer_class = UserSerializer
#
#     def perform_create(self, serializer):
#         queryset = User.objects.filter(user=self.request.user)
#         if queryset.exists():
#             raise ValidationError('You have already signed up')
#         serializer.save(user=self.request.user)

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
