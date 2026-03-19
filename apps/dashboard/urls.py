from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_home, name='home'),
    
    # News
    path('posts/', views.manage_posts, name='posts'),
    path('posts/add/', views.add_edit_post, name='add_post'),
    path('posts/edit/<int:pk>/', views.add_edit_post, name='edit_post'),
    path('posts/delete/<int:pk>/', views.delete_post, name='delete_post'),
    
    # Specific categories
    path('rajasthan-news/', views.rajasthan_news, name='rajasthan_news'),
    
    # Notices
    path('notices/', views.manage_notices, name='notices'),
    path('notices/add/', views.add_edit_notice, name='add_notice'),
    path('notices/edit/<int:pk>/', views.add_edit_notice, name='edit_notice'),
    path('notices/delete/<int:pk>/', views.delete_notice, name='delete_notice'),
    
    # Events
    path('events/', views.manage_events, name='events'),
    path('events/add/', views.add_edit_event, name='add_event'),
    path('events/edit/<int:pk>/', views.add_edit_event, name='edit_event'),
    path('events/delete/<int:pk>/', views.delete_event, name='delete_event'),
    
    # Gallery
    path('gallery/', views.manage_gallery, name='gallery'),
    path('gallery/add/', views.add_edit_album, name='add_album'),
    path('gallery/edit/<int:pk>/', views.add_edit_album, name='edit_album'),
    path('gallery/delete/<int:pk>/', views.delete_album, name='delete_album'),
    
    # Photos
    path('gallery/photos/', views.manage_photos, name='photos'),
    path('gallery/photos/add/', views.add_edit_photo, name='add_photo'),
    path('gallery/photos/edit/<int:pk>/', views.add_edit_photo, name='edit_photo'),
    path('gallery/photos/delete/<int:pk>/', views.delete_photo, name='delete_photo'),

    # Community
    path('community/', views.manage_community, name='community'),
    path('community/add/', views.add_edit_community, name='add_community'),
    path('community/edit/<int:pk>/', views.add_edit_community, name='edit_community'),
    path('community/delete/<int:pk>/', views.delete_community, name='delete_community'),
    
    
    # Members
    path('members/', views.manage_members, name='members'),
    path('members/approve/<int:pk>/', views.approve_member, name='approve_member'),
    path('members/delete/<int:pk>/', views.delete_member, name='delete_member'),
]
