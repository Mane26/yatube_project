from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Group title')
    slug = models.SlugField(unique=True, verbose_name='Relative URL')
    description = models.TextField(
        null=True, blank=True,
        verbose_name='Group description'
    )

    def _str_(self) -> str:
        return self.title


class Post(models.Model):
    # Тип: TextField
    text = models.TextField()
    # Тип поля: DateTimeField, для хранения даты и времени;
    # параметр auto_now_add определяет, что в поле будет автоматически
    # подставлено время и дата создания новой записи
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    # Тип: ForeignKey, ссылка на модель User
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )


class Meta:
    ordering = ('-pub_date',)
    default_related_name = 'posts'
