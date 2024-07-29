from django.urls import path

from blog.apps import BlogConfig
from blog.views import MainView, BlogListView, ReaderListView, BlogDeleteView, BlogUpdateView, BlogDetailView, \
    BlogCreateView

app_name = BlogConfig.name

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('list/', BlogListView.as_view(), name='list'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('content/<int:pk>', BlogDetailView.as_view(), name='view'),
    path('edit/<int:pk>', BlogUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name='delete'),
    path('post-list/', ReaderListView.as_view(), name='post_list'),
]
