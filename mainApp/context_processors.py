from .models import Dosage
from authApp.models import ProfilePic


def user_profile(request):
    if request.user.is_authenticated:
        current_user = request.user
        dosages = Dosage.objects.filter(user=current_user)
        profile_pic = ProfilePic.objects.get(user=current_user)
        return {
            "username": current_user,
            "dosages": dosages,
            "profile_pic": profile_pic.image.url,
        }
    else:
        return {}
