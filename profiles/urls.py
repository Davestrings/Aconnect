from django.urls import path
from .views import my_profile_view, invite_received_view, profile_list_view, profiles_i_can_invite, ProfileDetailView, ProfileListView, send_invitation, remove_from_friends, accept_invitation, reject_invitation

app_name = 'profiles'

urlpatterns = [
    path('', ProfileListView.as_view(), name='all_profiles'),
    path('myprofile/', my_profile_view, name='my_profile_view'),
    path('invites/', invite_received_view, name='invites'),
    path('invite_friends/', profiles_i_can_invite, name='invite_friends'),
    path('send-invite/', send_invitation, name='send-invite'),
    path('remove-friend/', remove_from_friends, name='remove-friend'),
    path('<slug>/', ProfileDetailView.as_view(), name='profile_detail_view'),
    path('invites/accept_invite', accept_invitation, name='accept_invite'),
    path('invites/reject_invite/', reject_invitation, name='reject_invite'),

]
