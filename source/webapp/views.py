import requests
from webapp.models import User
from django.shortcuts import render, redirect
from django.views.generic import DetailView


def index_view(request):
    return render(request, 'index.html')


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
    user = User.objects.create(all_user_data=user_data_for_mail, email=email_constructor, md5=md5, sha1=sha1,
                               sha256=sha256)
    return redirect('user_page', pk=user.pk)


class UserDetailView(DetailView):
    model = User
    template_name = 'user_page.html'
