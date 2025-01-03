from django.urls import path
from .views import LoginView, RegisterView, ProfileView, FollowUser, UnfollowUser
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
   path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', FollowUser.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUser.as_view(), name='unfollow-user'),
]