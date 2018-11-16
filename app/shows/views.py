from django.shortcuts import render, get_object_or_404, redirect

# 전체 리스트
from .forms import CommentForm
from .models import Show


def show_list(request):
    shows = Show.objects.all()
    content = {
        'shows': shows,
        'comment_form': CommentForm(),
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


# comment 작성
def comment_create(request, post_pk):
    if request.method == 'POST':
        show = Show.objects.get(pk=post_pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.show = show
            comment.save()
            comments = show.comments.all()
            content = {
                'show': show,
                'comments': comments,
            }
            return render(request, 'shows/show_detail.html', content)


def show_pick_toggle(request,show_pk):

    if request.method == 'POST':
        show = get_object_or_404(Show, pk=show_pk)
        show.pick_toggle(request.user)
        comments = show.comments.all()
        content = {
            'show': show,
            'comments': comments,
        }
        return render(request, 'shows/show_detail.html', content)