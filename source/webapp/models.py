from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Имя пользователя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилие пользователя')
    email = models.EmailField(verbose_name='Почтовый ящик')
    city = models.CharField(max_length=255, verbose_name='Город')
    country_code = models.CharField(max_length=255, verbose_name='Код страны')
    md5_letter = models.TextField(null=True, blank=True)
    sha1_letter = models.TextField(null=True, blank=True)
    sha256_letter = models.TextField(null=True, blank=True)
    md5 = models.TextField(null=True, blank=True)
    sha1 = models.TextField(null=True, blank=True)
    sha256 = models.TextField(null=True, blank=True)
    all_user_data = models.TextField(verbose_name='Все полученные данные', null=True, blank=True)

    def __str__(self):
        return "%s %s" % (self.last_name, self.first_name)
