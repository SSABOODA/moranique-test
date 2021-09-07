from rest_framework             import generics
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from .models import Blog
from .permissions import IsOwnerOrReadOnly
from .serializers import BlogSerializer


class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]


class BlogCreateView(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)


class BlogUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    permission_classes = [IsOwnerOrReadOnly]

