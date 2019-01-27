from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # post views

    # url pattern for function based view
    # path('', views.post_list, name='post_list'),

    # url pattern for class based view
    path('', views.PostListView.as_view(), name='post_list'),

    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
        views.post_detail,
        name='post_detail'),
]