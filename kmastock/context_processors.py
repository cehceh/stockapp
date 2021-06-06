from apps.accounts.views import UserProfile



def extras(request):
    match = UserProfile.objects.filter(user_id=request.user.id).exists()
    if match:
        qs = UserProfile.objects.get(user_id=request.user.id)
    else:
        qs = None
    context = {
        'match_user': match,
        'profile': qs,
    }
    return context


