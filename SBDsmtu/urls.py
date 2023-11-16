from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import *

urlpatterns = [
    path('',index,name='index'),
    # path('purchases/', views.purchase_list, name='purchase_list'),
    # path('handle_upload/', views.handle_upload, name='handle_upload'),
    path('add_purchase/', views.add_purchase, name='add_purchase'),
    path('success/', views.success, name='success'),
    path('delete_purchase/<int:purchase_id>/', views.delete_purchase, name='delete_purchase'),
    path('save_data/<int:purchase_id>/', views.save_data, name='save_data'),
    # path('sort_purchases/', views.purchase_list, name='purchase_list'),
    path('filter/', views.filter_purchase, name='filter_purchase'),
    path('analis/', views.analis, name='analis'),
    path('upload_csv/', views.upload_csv, name='upload_csv'),
   path('delete_selected_records/', views.delete_selected_records, name='delete_selected_records'),
    # path('search/', views.search_purchase, name='search_purchase'),
    # path('simple_post/', views.simple_post, name='simple_post'),
    path('simpl/', views.simpl, name='simpl'),
    path('login/', views.login_view, name='login'),
    path('registration/', views.registration, name='registration'),
    path('view_users/', view_users, name='view_users'),
    path('update_user_role/<int:user_id>/', update_user_role, name='update_user_role'),
     path('logout/', user_logout, name='user_logout'),
   
]