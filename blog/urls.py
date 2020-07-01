from django.urls import path
from .views import home
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView, PostDeleteView,UserPostListView,bootstrapfilterview,searchpage
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('filtering/', views.searchpage,name='search_page'),
    path('filter_result/',views.bootstrapfilterview, name='filter_result'),
    path('', views.searchpage, name='blog-home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    #pk is the expected value not id
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    #the above link expects post_form.html template as default
    #it shares with the post update view too
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    #it require post_confirm_delete.html template
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),


]


