from django.shortcuts import render
from .models import Profile, Relationship
from .forms import ProfileModelForm


# Create your views here.
def my_profile_view(request):
    # get profile of the current user
    profile = Profile.objects.get(user=request.user)
    form = ProfileModelForm(request.POST or None, request.FILES or None, instance=profile)
    confirm = False
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            confirm = True

    context = {
        'profile': profile,
        'form': form,
        'confirm': confirm,
    }
    return render(request, 'profile/myprofile.html', context)


def invite_received_view(request):
    profile = Profile.objects.get(user=request.user)
    query = Relationship.objects.invitations_received(profile)

    context = {
        'query': query,
    }
    return render(request, 'profile/invite.html', context)


def profile_list_view(request):
    user = request.user
    qs = Profile.objects.get_all_profiles(user)

    context = {
        'qs': qs,
    }

    return render(request, 'profiles/profile_list.html', context)


def profiles_i_can_invite(request):
    user = request.user
    query = Profile.objects.get_all_profiles_to_invite(user)

    context = {
        'query': query,
    }
    return render(request, 'profiles/to_invite_list.html', context)
