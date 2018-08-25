
from django.conf.urls import url
from django.contrib import admin
import nlpCoding.views

urlpatterns = [
	

	url(r'^$', nlpCoding.views.home, name="home"),
	url(r'^upload1/', nlpCoding.views.upload1, name="upload1"),
	url(r'^upload2/', nlpCoding.views.upload2, name="upload2"),
	url(r'^upload3/', nlpCoding.views.upload3, name="upload3"),
	url(r'^upload4/', nlpCoding.views.upload4, name="upload4"),
	
	url(r'^search1/', nlpCoding.views.search1, name="search1"),
	url(r'^search2/', nlpCoding.views.search2, name="search2"),	
	url(r'^search3/', nlpCoding.views.search3, name="search3"),	
	url(r'^search5/', nlpCoding.views.search5, name="search5"),	

    url(r'^admin/', admin.site.urls),
]
