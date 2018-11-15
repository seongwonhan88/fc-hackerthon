from django.shortcuts import render, get_object_or_404

# 전체 리스트
from .models import Show


def show_list(request):
    return render(request, 'shows/show_list.html')


# 전시회 상세보기
def show_detail(request, pk):
    show = get_object_or_404(Show, pk=pk)
    content = {
        'show': show,
    }

    return render(request, 'shows/show_detail.html', content)


# 특정 rating 이상 보기
def show_rating(request, rating_score):
    return render(request, 'show/show_rating.html')

