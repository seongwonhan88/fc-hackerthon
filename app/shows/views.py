from django.shortcuts import render, get_object_or_404

# 전체 리스트
from .models import Show


def show_list(request):
    shows = Show.objects.all()
    content = {
        'shows': shows,
    }
    return render(request, 'shows/show_list.html', content)


# 전시회 상세보기
def show_detail(request, show_pk):
    show = get_object_or_404(Show, pk=show_pk)
    comments = show.comments.all()
    content = {
        'show': show,
        'comments': comments,
    }

    return render(request, 'shows/show_detail.html', content)


# 특정 rating 이상 보기
def show_rating(request, rating_score):
    return render(request, 'show/show_rating.html')

