from django.urls import path
from .views import my_profile_view, invite_received_view, profile_list_view, profiles_i_can_invite

app_name = 'profiles'

urlpatterns = [
    path('myprofile/', my_profile_view, name='my_profile_view'),
    path('invites/', invite_received_view, name='invites'),
    path('allprofiles/', profile_list_view, name='allprofiles'),
    path('invite_friends/', profiles_i_can_invite, name='invite_friends'),
]
