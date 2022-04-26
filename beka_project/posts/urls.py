from django.urls import path
from posts import views
from .views import *
urlpatterns = [
    path('registration/', createuser, name="create_user"),
    path('', views.index2,name="index2"),
    path('index',views.index,name="index"),
    path('upload/', views.upload, name='upload-posts'),
    path('update/<int:post_id>', views.update_post),
    path('delete/<int:post_id>', views.delete_post),
    path('discount', views.discount,name="discount"),
    path('firstPage', views.firstPage,name="firstPage"),
    path('places', views.places,name="places"),
    path('services', views.services,name="services"),
    ]