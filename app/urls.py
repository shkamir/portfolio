from django.conf.urls import url
from .views import ProjectListAndFormView


app_name='main'
urlpatterns = [
    url(r'^$', ProjectListAndFormView.as_view(), name='main')
]
