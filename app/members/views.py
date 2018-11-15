from django.shortcuts import render


def login_view(request):
    return render(request, 'members/login.html')


# 사용자가 찜한 목록 보
def user_pick(request, pk):
    return render(request, 'members/user_pick.html')
