from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'app1' # to diferentiate in case I have more than 1 app
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.DetailView.as_view(), name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
	# Add Django site authentication urls (for login, logout, password management)
	#url(r'^accounts/login/$',views.login,name='login'),
    #url(r'^login/$',auth_views.login, {'template_name': 'login.html'}),
]