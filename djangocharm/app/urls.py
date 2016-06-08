from django.conf.urls import url

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', 'app.views.base',name='3'),
    url(r'^list/$', 'app.views.themelist'),
    url(r'^subjectlist/$', 'app.views.subjectlist'),
    url(r'^profile/$', 'app.views.profile'),
    url(r'^leaderboard/$', 'app.views.leaderboard_redirect'),
    url(r'^leaderboard/(?P<page_no>\d+)/$', 'app.views.leaderboard'),

]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)