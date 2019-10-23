from django.urls import path
from . import views
app_name='board'

urlpatterns = [
    path('' , views.index, name='index'),
    path('create/', views.create, name='create'),

    path('<int:id>/', views.detail, name='detail'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('<int:id>/update/', views.update, name='update'),

    path('<int:id>/create/c', views.create_c, name='create_c'),
    path('<int:p_id>/delete/<int:c_id>/', views.delete_c, name='delete_c'),

    path('search/', views.search, name='search'),
    
    path('<int:id>/like/', views.like, name="like" ),
    path('<int:p_id>/like/<int:c_id>/', views.like_c, name="like_c")
]
