from django.conf.urls import url

from center.views import CenterHome


urlpatterns = [
    url(r'^home/(?P<user_id>\d+)', CenterHome.as_view(), name='home'),
]