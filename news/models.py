from django.db import models

class Articles(models.Model): # Таблица баз данных
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):      # Это чтобы удобно выводились названия таблиц
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta: # Название, которое будет высвечиваться в базе данный на странице admin
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'