from django.contrib.auth import logout
from django.shortcuts import render, redirect


def login_view(request):
    return render(request, 'members/login.html')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('shows:show-list')
    else:
        pass


# 사용자가 찜한 목록 보
def user_pick(request, pk):
    return render(request, 'members/user_pick.html')
