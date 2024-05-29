# from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from django.contrib.auth.models import User

# Create your views here.
class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            print('encontrado')
            author = self.request.user
        else:
            print('no encontrado')
            author_data = self.request.data.get('author')
            if author_data:
                try: 
                    author = User.objects.get(id=author_data)
                except User.DoesNotExist:
                    author = None
            else:
                author = None
        serializer.save(author=author)


        #     print('nadie identificado')
        #     author = None
        # serializer.save(author=author)

class PostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer