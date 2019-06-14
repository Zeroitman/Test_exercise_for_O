import requests
from webapp.models import User
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
import re
import yandex.Translater as T


def index_view(request):
    return render(request, 'index.html')


def instruction_page(request):
    return render(request, 'instruction.html')


class AnytextLatin():
    def __init__(self, first_name, last_name, city):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city

    def in_latin(self, text):
        tr = T.Translater()
        tr.set_key('trnsl.1.1.20190614T100357Z.bc5cd3d6c2ce136a.74da88f3d7becf09a42fdedd209fdce78f9c7599')
        tr.set_text(text)
        tr.detect_lang()
        tr.set_to_lang('en')
        return tr.translate()

    def first_name_text(self):
        return self.in_latin(self.first_name)

    def last_name_text(self):
        return self.in_latin(self.last_name)

    def city_text(self):
        return self.in_latin(self.city)


class Separation():
    def __init__(self, md5, sha1, sha2):
        self.md5 = md5
        self.sha1 = sha1
        self.sha2 = sha2

    def all(self, hash):
        number_in = re.findall(r'\d+', hash)
        str_in = re.findall(r'\D+', hash)
        conv_number_in, conv_str_in = ''.join(number_in), ''.join(str_in)
        conv_number_and_string = conv_number_in + conv_str_in
        return conv_number_and_string

    def separation_md5(self):
        return self.all(self.md5)

    def separation_sha1(self):
        return self.all(self.sha1)

    def separation_sha2(self):
        return self.all(self.sha2)


def get_user(request):
    user_data_for_mail = requests.get("https://randomuser.me/api?nat=ir").json()
    first_name = user_data_for_mail['results'][0]['name']['first']
    last_name = user_data_for_mail['results'][0]['name']['last']
    city = user_data_for_mail['results'][0]['location']['city']
    country_code = user_data_for_mail['results'][0]['nat']
    md5 = user_data_for_mail['results'][0]['login']['md5']
    sha1 = user_data_for_mail['results'][0]['login']['sha1']
    sha256 = user_data_for_mail['results'][0]['login']['sha256']
    a = Separation(md5=md5, sha1=sha1, sha2=sha256)
    md5_ready = a.separation_md5()
    sha1_ready = a.separation_sha1()
    sha256_ready = a.separation_sha2()
    b = AnytextLatin(first_name=first_name, last_name=last_name, city=city)
    first_name_ready = b.first_name_text()
    last_name_ready = b.last_name_text()
    city_ready = b.city_text()
    email_constructor = first_name_ready[0:2] + last_name_ready + '@' + city_ready + '.' + country_code.lower()
    user = User.objects.create(all_user_data=user_data_for_mail,
                               email=email_constructor.replace(' ', '').lower(),
                               md5=md5_ready,
                               sha1=sha1_ready,
                               sha256=sha256_ready,
                               first_name=first_name_ready.capitalize(),
                               last_name=last_name_ready.capitalize(),
                               city=city_ready.capitalize(),
                               country_code=country_code)
    return redirect('user_page', user.pk)


class UserDetailView(DetailView):
    model = User
    template_name = 'user_page.html'


class UserListView(ListView):
    model = User
    template_name = 'all_user.html'
