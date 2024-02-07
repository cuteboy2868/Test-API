from django.urls import path
from .views import *


urlpatterns = [
    path('index/', index_view, name='index_url'),
    path('about-page/', about_view, name='about_url'),
    path('news-page/', news_page_view, name='news_page_url'),
    path('contact-page/', contact_view, name='contact_page_url'),
    path('', login_user, name='login_user_url'),
    path('register-page/', register_user, name='register_user_url'),
    path('shop-page/', shop_page_view, name='shop_page_url'),
    path('my-profile/<int:pk>/', profile_view, name='profile_url'),
    path('user-delete/<int:pk>/', user_delete, name='user_delete_url'),
    path('log-out/', logout, name='logout_url')
]