from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Имя пользователя', null=True, blank=True)
    last_name = models.CharField(max_length=255, verbose_name='Фамилие пользователя', null=True, blank=True)
    email = models.EmailField(verbose_name='Почтовый ящик', null=True, blank=True)
    md5 = models.TextField(verbose_name='Разделённый md5', null=True, blank=True)
    sha1 = models.TextField(verbose_name='Разделённый sha1', null=True, blank=True)
    sha256 = models.TextField(verbose_name='Разделённый sha256', null=True, blank=True)
    all_user_data = models.TextField(verbose_name='Все полученные данные')

    def __str__(self):
        return "%s %s" % (self.last_name, self.first_name)
