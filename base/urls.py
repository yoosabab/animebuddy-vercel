from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name="login_page"),
    path('logout/', views.logout_user, name="logout_user"),
    path('register/', views.register_page, name="register"),
    path('update-user/', views.update_user, name="update_user"),
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('room/<str:pk>/send/', views.send_message, name="send"),
    path('room/<str:pk>/get/', views.get_message, name="get"),
    path('profile/<str:pk>/', views.user_profile, name="user_profile"),
    path('create-room/', views.create_room, name="create_room"),
    path('update-room/<str:pk>/', views.update_room, name="update_room"),
    path('delete-room/<str:pk>/', views.delete_room, name="delete_room"),
    path('delete-message/<str:pk>/', views.delet_message, name="delet_message"),
    path('topics/', views.topic_page, name="topics"),
    path('activity/', views.activity_page, name="activity"),
]
