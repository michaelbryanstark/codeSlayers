from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
 path('', views.Home.as_view(), name="home"),
 path('accounts/signup/', views.Signup.as_view(), name="signup"),
 path('profile/', views.Profile.as_view(), name="profile"),
 path('cities/', views.CityList.as_view(), name="city_list"),
 path('cities/posts/<int:pk>/', views.PostDetail.as_view(), name="post_detail"),
 path('cities/<int:pk>/', views.CityDetail.as_view(), name="city_detail"),
 path('posts/<int:pk>/delete', views.PostDelete.as_view(), name="post_delete"),
 path('posts/new/', views.PostCreate.as_view(), name="post_create"),
 path('cities/new/', views.CityCreate.as_view(), name="city_create"),
]