from django.db import models


class User(models.Model):
    all_user_data = models.TextField(verbose_name='Пользователь')
    email = models.EmailField(verbose_name='Почтовый ящик', null=True, blank=True)
    md5 = models.TextField(verbose_name='md5', null=True, blank=True)
    sha1 = models.TextField(verbose_name='sha1', null=True, blank=True)
    sha256 = models.TextField(verbose_name='sha256', null=True, blank=True)

    def __str__(self):
        return "%s" % self.all_user_data

