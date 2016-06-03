from django.conf.urls import url
from .views import *

urlpatterns = [
  url(r'^new$', create_new_course, name='create_new_course'),
  url(r'^edit', course_edit, name='course_edit'),
  url(r'^lecture/new$', new_lecture, name='new_lecture'),
  url(r'^lecture/edit', edit_lecture, name='edit_lecture'),
  url(r'^lectures$', lectures, name='lectures'),
  url(r'^lecture', get_lecture, name='lectures'),
  url(r'^$', home, name='home'),
  url(r'^', go_to_course, name='go_to_course'),

]
