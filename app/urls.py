# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    
    path('video_feed', views.video_feed, name='video_feed'),
    
    path('webcam_feed', views.webcam_feed, name='webcam_feed'),
    
    path('media', views.media, name='media'),
    
    path('check_image', views.check_image, name='check_image'),
    
    path('video_names', views.video_names, name='video_names'),
    
    path('delete_from_db', views.delete_from_db, name='delete_from_db'),
    
    path('add_to_database', views.add_to_database, name='add_to_database'),

    path('edit_person', views.edit_person, name='edit_person'),
    
    path('check_length', views.check_length, name='check_length'),
    
    path('add_single_image', views.add_single_image, name='add_single_image'),
    
    path('check_single_image', views.check_single_image, name='check_single_image'),
    

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
   

]