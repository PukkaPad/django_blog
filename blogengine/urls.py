from django.conf.urls import url
from django.views.generic import ListView
from blogengine.models import Post

urlpatterns = [
    # Index
    url(r'^(?P<page>\d+)?/?$', ListView.as_view(
        model=Post,
        paginate_by=5,
        ),
        name='index'
        ),
]