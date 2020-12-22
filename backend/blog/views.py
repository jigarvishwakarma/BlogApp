from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from blog.models import BlogPost,BlogBook
from blog.serializers import BlogPostSerializer,BlogBookSerializer

class BlogPostListView(ListAPIView):
    queryset = BlogPost.objects.order_by('-date_created')
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class BlogPostDetailView(RetrieveAPIView):
    queryset = BlogPost.objects.order_by('-date_created')
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class BlogPostFeaturedView(ListAPIView):
    queryset = BlogPost.objects.all().filter(featured=True)
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class BlogPostCategoryView(APIView):
    serializer_class = BlogPostSerializer
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data
        category = data['category']
        queryset = BlogPost.objects.order_by('-date_created').filter(category__iexact=category)

        serializer = BlogPostSerializer(queryset, many=True)

        return Response(serializer.data)

class BlogBooktListView(ListAPIView):
    queryset = BlogBook.objects.order_by('-date_created')
    serializer_class = BlogBookSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class BlogBookDetailView(RetrieveAPIView):
    queryset = BlogBook.objects.order_by('-date_created')
    serializer_class = BlogBookSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )