from django.contrib.auth import logout
from django.shortcuts import render, redirect

from shows.models import Show, ShowPick


def login_view(request):
    return render(request, 'members/login.html')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('shows:show-list')
    else:
        pass


# 사용자가 찜한 목록 보기
def user_pick(request):
    picked_shows = ShowPick.objects.filter(user=request.user)
    return render(request, 'members/user_pick.html', {"picked_shows":picked_shows})
