from django.urls import path
from blog.views import BlogPostListView, BlogPostDetailView, BlogPostFeaturedView, BlogPostCategoryView,BlogBooktListView,BlogBookDetailView

urlpatterns = [
	path('book', BlogBooktListView.as_view(),name='booklist'),
    path('', BlogPostListView.as_view(),name='booklist'),
    path('featured', BlogPostFeaturedView.as_view(),name='featured'),
    path('category', BlogPostCategoryView.as_view(),name='category'),
    path('<slug>', BlogPostDetailView.as_view(),name='detail'),
    path('blogbook/<slug>', BlogBookDetailView.as_view(),name='bookdetail'),
]
