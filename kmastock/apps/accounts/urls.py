from django.urls import path
from django.contrib.auth import views as auth_views
from .views import edit_user_profile, add_user_profile
# UserProfilePageView,

app_name = 'accounts'

urlpatterns = [
    # previous login view
    # path('login/', views.user_login, name='login'),
    
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('profile/<profile_uuid>/', UserProfilePageView.as_view(), name='user_profile'), # profile page views
    path('profile/user/id/<user_id>/unique/id/<uuid>/', edit_user_profile, name='edit_user_profile'), # profile page views
    path('profile/user/id/<user_id>/', add_user_profile, name='add_user_profile'), # profile page views
]