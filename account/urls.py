from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # path('login/',views.user_login,name='login'),
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('',views.dashboard,name='dashboard'),
    path('register/',views.register,name='register'),
    path('edit/',views.edit,name='edit'),
    path('users/',views.user_list,name='user_list'),
    path('users/follow/',views.user_follow,name='user_follow'),
    path('users/<username>/',views.user_detail,name='user_detail'),
]