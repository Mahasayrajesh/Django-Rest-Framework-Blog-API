from django.urls import path
from blog.views import PostListCreate, PostDetailUpdateDelete, CommentListCreate, CommentDetailUpdateDelete, RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from blog import views

urlpatterns = [
    path('posts/', PostListCreate.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailUpdateDelete.as_view(), name='post-detail'),
    path('comments/', CommentListCreate.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetailUpdateDelete.as_view(), name='comment-detail'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register')
]




