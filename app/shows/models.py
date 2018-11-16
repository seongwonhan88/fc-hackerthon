from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()
# Create your models here.


class Show(models.Model):
    title = models.CharField('전시명', max_length=50)
    period = models.CharField('전시기간', max_length=200)
    place = models.CharField('전시장소', max_length=200)
    thumbnail = models.ImageField('썸네일', upload_to='thumbnail')
    poster = models.ImageField('포스터', upload_to='poster')
    description = models.TextField('상세설명', blank=True, null=True)
    price = models.PositiveIntegerField('가격', default=0)
    created_at = models.DateTimeField('작성일자', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '전시'
        verbose_name_plural = f'{verbose_name} 목록'
        ordering = ['-pk']

    def pick_toggle(self, user):
        # 전달받은 user가 이 전시회를 이미 pick했다면 pick 해제
        # 안되어있다면 pick처리
        showpick, showpick_created = self.showpick_set.get_or_create(user=user)
        if not showpick_created:
            showpick.delete()

    pick_users = models.ManyToManyField(
        User,
        through='ShowPick',
        related_name='pick_shows',
        related_query_name='pick_show',
    )


class Comment(models.Model):
    show = models.ForeignKey(
        Show,
        on_delete=models.CASCADE,
        verbose_name='전시회',
        related_name='comments',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='작성자',
    )
    content = models.TextField('댓글 내용')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '댓글'
        verbose_name_plural = f'{verbose_name} 목록'

    def __str__(self):
        return f'[{self.author.username}]이/가 글[{self.show.title}]에 댓글: {self.content}'


class ShowPick(models.Model):
    show = models.ForeignKey(
        Show,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # 특정 User가 특정 전시회를 Pick한 정보는 unique해야함
        unique_together = (
            ('show', 'user'),
        )

    def __str__(self):
        return f'[{self.user.username}]이/가 [{self.show.title}]를 찜'


class Rating(models.Model):
    show = models.ForeignKey(
        Show,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    # 나중에 최고점 5 점으로 수정하는 알고리즘을 넣어야
    score = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # 특정 User가 특정 전시회를 rating한 정보는 unique해야함
        unique_together = (
            ('show', 'user'),
        )

    def __str__(self):
        return f'[{self.user.username}]이 [{self.show.title}]에 {self.score}점 줌 '
