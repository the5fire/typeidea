from django.conf.urls import url
from practice import views

urlpatterns = (
    url(r'^$', views.index, name='index'),
)
