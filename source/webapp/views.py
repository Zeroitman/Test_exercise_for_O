import requests
from webapp.models import User
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
import re


def index_view(request):
    return render(request, 'index.html')


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
    user_data_for_mail = requests.get("https://randomuser.me/api/?nat=us").json()
    first_name = user_data_for_mail['results'][0]['name']['first']
    last_name = user_data_for_mail['results'][0]['name']['last']
    city = user_data_for_mail['results'][0]['location']['city']
    country_code = user_data_for_mail['results'][0]['nat']
    md5 = user_data_for_mail['results'][0]['login']['md5']
    sha1 = user_data_for_mail['results'][0]['login']['sha1']
    sha256 = user_data_for_mail['results'][0]['login']['sha256']
    email_constructor = first_name[0:2] + last_name + '@' + city + '.' + country_code.lower()
    a = Separation(md5=md5, sha1=sha1, sha2=sha256)
    md5_ready = a.separation_md5()
    sha1_ready = a.separation_sha1()
    sha256_ready = a.separation_sha2()
    user = User.objects.create(all_user_data=user_data_for_mail,
                               email=email_constructor.replace(' ', ''),
                               md5=md5_ready,
                               sha1=sha1_ready,
                               sha256=sha256_ready,
                               first_name=first_name.capitalize(),
                               last_name=last_name.capitalize())
    return redirect('user_page', pk=user.pk)


class UserDetailView(DetailView):
    model = User
    template_name = 'user_page.html'


class UserListView(ListView):
    model = User
    template_name = 'all_user.html'
